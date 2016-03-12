import multiprocessing
from threading import *
import time
import random

#BUF_SIZE = 10
#queue =0
#count = 0


pc_queue = []
buff_size = 10
condition = Condition()


class Producer(Thread):
    def run(self):
        nums = range(5)
        global pc_queue
        while True:
            condition.acquire()
            if len(pc_queue) == buff_size:
                print ("Queue full, producer is waiting")
                condition.wait()
                print ("Space in queue, Consumer notified the producer")
            num = random.choice(nums)
            pc_queue.append(num)
            print("Produced", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


class Consumer(Thread):
    def run(self):
        global pc_queue
        while True:
            condition.acquire()
            if not pc_queue:
                print ("Nothing in queue, consumer is waiting")
                condition.wait()
                print ("Producer added something to queue and notified the consumer")
            num = pc_queue.pop(0)
            print ("Consumed", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


Producer().start()
Consumer().start()


#if __name__ == ‘__main__’:
    #q = multiprocessing.Queue()
    # launch the consumer process
    #cons_p = multiprocessing.Process(target=consumer, args=(q,))
    #cons_p.start()
    # produce items sequence = [1, 2, 3, 4] producer(sequence, q)
    # signal completion by putting the sentinel on the queue q.put(None)
    # wait for the consumer process to shutdown cons_p.join()
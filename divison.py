import multiprocessing def consumer(input_q):
pass
def producer(sequence, output_q):
pass
if __name__ == ‘__main__’:
q = multiprocessing.Queue()
# launch the consumer process
cons_p = multiprocessing.Process(target=consumer, args=(q,))
cons_p.start()
# produce items sequence = [1, 2, 3, 4] producer(sequence, q)
# signal completion by putting the sentinel on the queue q.put(None)
# wait for the consumer process to shutdown cons_p.join()

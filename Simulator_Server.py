
# server.py
import socket
import time
from threading import Thread
import threading
import sys
import subprocess

#TCP_IP = '23.253.20.67'
port = 5000
threadQueue = {}
count = 0
threadId = 0
bContinue = True

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
print(host)
print(port)
my_ip = subprocess.Popen(['ifconfig eth0 | awk "/inet /" | cut -d":" -f 2 | cut -d" " -f1'], stdout=subprocess.PIPE, shell=True)
(IP, errors) = my_ip.communicate()
my_ip.stdout.close()
print(IP)


def counter():
    global count
    global bContinue
    while True:
        if bContinue:
            count += 1
            time.sleep(3)
            print(count)
# bind to the port
s.bind((str(IP).strip(), port))

# queue up to 5 requests
s.listen()

t = Thread(target=counter,args=())
t.start()
lock = threading.Lock()


def clientThread(conn,threadID):
    global count
    global t
    global threadQueue
    global bContinue
    while True:
        command = conn.recv(32)
        val=command.decode()
        if val == 'get':
            lock.acquire()
            conn.send(str(count).encode())
            lock.release()
        elif 'set' in val:
            lock.acquire()
            count = int(val.split()[1])
            lock.release()
        elif 'stop' in val:
            lock.acquire()
            bContinue = False
            lock.release()
        elif 'continue' in val:
            lock.acquire()
            bContinue=True
            lock.release()
        else:
            try:
                lock.acquire()
                conn.close()
                lock.release()
                break

            except:
                print(sys.exc_info()[0])



    #conn.close()

while True:
    # establish a connection
    clientsocket,addr = s.accept()
    #print addr[0] + str(addr[1])

    print("Got a connection from %s" % str(addr))
    #currentTime = time.ctime(time.time()) + "\r\n"
    #clientsocket.send(currentTime.encode('ascii'))
    try:
     tClient = Thread(target=clientThread,args=(clientsocket,threadId))
     tClient.start()
     threadQueue[threadId] = tClient
     threadId = threadId+1
    except:
        print(sys.exc_info()[0])

    #s.shutdown(clientsocket)

s.close();
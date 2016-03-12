from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)  # Create TCP Socket
s.bind(('',8888))  # bind to port 8888
s.listen(5)  # 5 host can connect

while True:
    client, addr = s.accept()  #get connect
    print('got a connection from %s' % str(addr))
    timestr=time.ctime(time.time())+"\r\n"
    client.close()



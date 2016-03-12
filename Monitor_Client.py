# client.py
import socket
import sys

# Receive no more than 1024 bytes
#tm = s.recv(1024)
print (' 1. connect to the simulator by monitor <hostname>, Enter IP address to connect with Simulator_Server:  \
\n 2. change the count by set <number> \
\n 3. get the current count by get \
\n 4. stop the simulator by stop \
\n 5. resume the simulator by continue \
\n 6. disconnect to the simulator by quit')

command = input("Hint: Look in Simulator_Server output. Enter server <ip>: ")
#if command == connect to hostname
#if command != '23.253.20.67':
#    print('Please enter correct IP address, Hint: 23.253.20.67')

try:
#create an AF_INET, STREAM socket (TCP)
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print('Failed to create socket. Error code: ' + str([0]) + ' , Error message : ' + str([1]))
    sys.exit()

print('Socket Created')

#host = '23.253.20.67'
port = input("Hint: Look in Simulator_Server output. Enter server Port number: ")

#try:
#    remote_ip = socket.gethostbyname(command)

#except socket.gaierror:
    #could not resolve
#    print ('Hostname could not be resolved. Exiting')
#    sys.exit()

#print('Ip address of host is ' + remote_ip)

#Connect to remote server
c.connect((command, int(port)))

print('Socket Connected to host on ip ' + command)

while 1:

    command = input("Enter your command: ")

    if command == 'get':
        c.send(b'get')
        data = c.recv(32)
        print ("Received from Simulator_server: " + str(data.decode()))
    elif 'set' in command:
        check=(command.split()[1])
        try:
            check = int(check)
            c.send(command.encode())
        except ValueError:
            print("That's not an int number!")
    elif 'stop' in command:
        c.send(command.encode())
    elif 'continue' in command:
        c.send(command.encode())
    elif 'quit' in command:
        c.send(command.encode())
        c.close()
        break
    else:
        print('Please select only from above option')


#print("The time got from the server is %s" % tm.decode('ascii'))

'''
        serverIP = input("Enter IP address to connect with Simulator_Server:  ")
        # create a socket object
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        #host = socket.gethostname()

        port = 5000

        # connection to hostname on the port.
        c.connect((serverIP, port))
'''
import socket
import time
import pickle


## size allocated to tell the length of the msg
HEADERSIZE=10

msg="Welcome to the server"

## ecapsulate the first 10 byes for the header
msg=f'{len(msg):<{HEADERSIZE}}' + msg

#setting up a TCP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# bind the the socket to localHost
socket.bind(('localhost',1235))

## making a socket queue of 5 connections
## listen socket for client
socket.listen(5)

while True:
    ## wait for the client to be accepted
    clientsocket,address=socket.accept()

    print(f'connected to the client{address}');

    clientsocket.send(bytes(msg,"utf-8"))

    ## send the time to the client after every 3 seconds
    while(True):
        time.sleep(3)
        msg=f'The time is {time.time()}'
        msg=f'{len(msg):<{HEAERSIZE}}'+msg
        print(msg)
        clientsocket.send(bytes(msg,"utf-8"))
    ##closing the connnection
    # clientsocket.close()

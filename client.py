import socket

HEADERSIZE=10
## declaring a socket of type TCP and IPV4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## establish the connnection
s.connect(('localhost', 1235))


mymsg=''
## when server sends a new msg
new_msg=True
while (1):
  while(1):
     ## receive the bytes
     msg = s.recv(16)
     ## when new msg from server received
     if new_msg == True:
         ## check for the msg size
         print("size of msg is ", msg[:HEADERSIZE].decode("utf-8"))
         msg_size=int(msg[:HEADERSIZE].decode("utf-8"))
         new_msg=False
         ## only save the msg without the header
         mymsg=msg[HEADERSIZE:].decode("utf-8")

     else:
         mymsg+=msg.decode("utf-8")
     ## entire msg by the server read
     if len(mymsg) == msg_size:
       new_msg=True
       print(mymsg)





print(mymsg)

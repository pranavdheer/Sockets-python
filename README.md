# Sockets-python

### Server.py
The server scripts creats a socket at the LocalHost, connects to the client and sends the time after every 3 seconds
The message is sent along with a message header which stores the message size

### client.py
the client script has a buffer to read server response, and uses the message header to deduce the size of the message which has to be read ( so it knows when to stop reading)

### NOTE-: The code is adapted from https://pythonprogramming.net/sockets-tutorial-python-3/



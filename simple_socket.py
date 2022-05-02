import socket

# Creates a socket object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects the socket to the server at data.pr4.org on port 80
mysock.connect(('data.pr4e.org', 80))

"""Sends a command to get the data from http://data.pr4e.org/page1.htm
Also contains the request header HTTP/1.0\r\n\r\n
"""
command = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# Tells the socket to send the command
mysock.send(command)

# Runs a while loop if the connection is open to send the data and if the data is less than 1 it breaks the connection and if its true decodes the data in unicode format from the utf-8 encoding format
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Closes the socket connection
mysock.close()
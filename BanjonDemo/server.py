__author__ = 'lizhengning1'
import sys
import getopt
import socket
import select
import json

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 9999))
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.listen(5)
socks = [serversocket, sys.stdin]

while True:
    readable, writable, exceptionavailable = select.select(socks,[],[])
    for sock in readable:
        if sock == serversocket:
            ClientSock, ClientAddr = serversocket.accept()
            socks.append(ClientSock)
        elif sock == sys.stdin:
            continue
        else:
            data = sock.recv(4096)
            if len(data) > 0:
                data = json.loads(data)
                print data

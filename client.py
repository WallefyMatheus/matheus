#!/usr/bin/env python3

import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])

if ':' in HOST :
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
else :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
message = 1
s.sendall( message.to_bytes(2, byteorder='big') )
data = s.recv(1024)

print('Received', repr(data))

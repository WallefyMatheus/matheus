#!/usr/bin/env python3

import socket
import sys
import os

BUFFER_SIZE = 1000

HOST = sys.argv[1]
PORT = int(sys.argv[2])
filename = sys.argv[3]

if ':' in HOST :
    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
else :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
message = 1
s.sendall( message.to_bytes(2, byteorder='big') )
data = s.recv(1024)
message_received_type = int.from_bytes(data[0:2], byteorder='big')
message_received_port = int.from_bytes(data[2:6], byteorder='big')
print('Received', message_received_type,message_received_port)

if ':' in HOST :
    s_udp = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
else :
    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_udp.bind((HOST,message_received_port))

if len(filename) < 16 and filename[len(filename)-4] == '.' and filename.count('.') == 1 :
    message = (3).to_bytes(2, byteorder='big')
    filesize = os.path.getsize(filename)
    print(filesize)

    sys.exit()

    message = message + filename.encode()
    s.sendall( message )
    data = s.recv(1024)
    message_received_ok = int.from_bytes(data, byteorder='big')
    if message_received_ok == 4 :
        print('Received', message_received_ok)
        f = open(filename, "rb")

        i = 0
        while True :
            message = (6).to_bytes(2, byteorder='big')
            payload = f.read(BUFFER_SIZE)
            if len(payload) == 0 :
                break
            else :
                message = message + i.to_bytes(4, byteorder='big') + len(payload).to_bytes(2, byteorder='big') + payload
                s_udp.sendall( message )
                i += 1
else :
    print("Nome não permitido")

#!/usr/bin/env python3

import socket
import sys
import _thread

BUFFER_SIZE = 1000

HOST = '::1'
PORT = int(sys.argv[1])

s = socket.create_server((HOST,PORT), family=socket.AF_INET6, dualstack_ipv6=True)

def multi_thread(conn,s) :
    print('Connected by', addr)
    data = conn.recv(1024)
    if int.from_bytes(data, byteorder='big') == 1 :
        message = (2).to_bytes(2,byteorder='big')
        if ':' in addr[0] :
            s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        else :
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        s.bind((HOST,0))
        port_udp = s.getsockname()[1]
        message = message + port_udp.to_bytes(4,byteorder='big')
        conn.sendall(message)

        data = conn.recv(1024)

        sys.exit()

        if int.from_bytes(data[0:2], byteorder='big') == 3 :
            message = (4).to_bytes(2,byteorder='big')
            conn.sendall(message)

        while True :
            data = conn.recv(BUFFER_SIZE)


        else :
            print('[LOG] Erro no recebimento da mensagem de INFO FILE')
    else :
        print('[LOG] Erro no recebimento da mensagem de HELLO')


while True:
    conn, addr = s.accept()
    _thread.start_new_thread(multi_thread, (conn,s))

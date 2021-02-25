#!/usr/bin/env python3

import socket
import sys
import _thread

# HOST_IPV4 = '127.0.0.1'
# HOST_IPV6 = '::1'

HOST = '::1'
PORT = int(sys.argv[1])

s = socket.create_server(HOST, *, family=AF_INET6, backlog=None, reuse_port=False, dualstack_ipv6=True)

# s_tcp4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s_tcp6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# s_tcp4.bind((HOST_IPV4, PORT))
# s_tcp4.listen()
#
# s_tcp6.bind((HOST_IPV6, PORT,0,0))
# s_tcp6.listen()

def multi_thread(conn,s_tcp) :
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        if int.from_bytes(data, byteorder='big') == 1 :
            message = 2
            conn.sendall(message.to_bytes(2, byteorder='big'))
            if ':' in addr[1] :
                s_udp = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            else :
                s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else :
            print('[LOG] Erro no recebimento da mensagem de HELLO')

def accept_tcp6(s, null) :
    print("OI")
    while True:
        conn, addr = s.accept()
        _thread.start_new_thread(multi_thread, (conn,s))


_thread.start_new_thread(accept_tcp4, (s,' '))
print('Cabo')

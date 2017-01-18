# -*- coding: utf-8 -*-

import socket
import threading
import time

def tcp_process(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send((data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print ('Connection from %s:%s closed' % addr)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 9999))
    s.listen(5)
    print ('waiting for connecting...')

    while True:
        conn, addr = s.accept()

        t = threading.Thread(target=tcp_process, args=(conn, addr))
        t.start()

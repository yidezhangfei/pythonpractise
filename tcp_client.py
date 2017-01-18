# -*- coding: utf-8 -*-

import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('139.199.36.63', 9999))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        s.send(data)
        recv_data = s.recv(1024).decode('utf-8')
        print (recv_data)
    s.send(b'exit')
    s.close()

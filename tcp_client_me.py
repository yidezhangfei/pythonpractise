# -*- coding: utf-8 -*-

import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('139.199.36.63', 9999))
    print(s.recv(1024).decode('utf-8'))
    while True:
        data = input()
        s.send(data.encode('utf-8'))
        if data == 'exit':
            break
        recv_data = s.recv(1024).decode('utf-8')
        print (recv_data)
    s.close()

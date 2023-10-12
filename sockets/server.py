#!/usr/bin/python3
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('' , 4080))

    while 1:
        msg, addr = s.recvfrom(1024)
        msg = msg.decode('ascii', 'replace')

        # Alternative way to handle errors in decoding:
        # try:
        #     msg, addr = s.recvfrom(1024)
        #     msg = msg.decode('ascii')
        # except UnicodeDecodeError as e:
        #     print(f'Error from {addr}: ')
        #     print(e)
        #     continue

        print(f'Got data "{msg}" from {addr}')

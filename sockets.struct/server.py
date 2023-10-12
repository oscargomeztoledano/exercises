#!/usr/bin/python3
import socket
import struct


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('' , 12345))

    while True:
        data, addr = s.recvfrom(1024)
        l, = struct.unpack('!h', data[:2])
        word, = struct.unpack('!' + str(l) + 's', data[2:])
        print(f'Got "{word.decode()}" ({l} bytes)')

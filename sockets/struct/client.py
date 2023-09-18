#!/usr/bin/python3
import socket
import struct
import random


words = ['hello world', 'meh', 'struct', "ñandú"]
word = random.choice(words).encode()
l = len(word)
format = f'!h{str(l)}s'

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    data = struct.pack(format, len(word), word)
    s.sendto(data, ('localhost', 12345))

#!/usr/bin/python3
import sys
import socket

host, port = sys.argv[1].split(':')
msg = sys.argv[2]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(msg.encode(), (host, int(port)))

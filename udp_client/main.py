#!/usr/bin/python3

# Just simple UDP client made using 'socket' module
# This project was created only for learning and will not be developed any more.
# Author: D1N3SHh


import socket

target_host = ""
target_port = 0

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("data".encode(), (target_host, target_port))

data, addr = client.recvfrom(4096)
print(data)
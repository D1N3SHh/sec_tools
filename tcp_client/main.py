#!/usr/bin/python3

# Just simple TCP client made using 'socket' module
# This project was created only for learning and will not be developed any more.
# Author: D1N3SHh


import socket

target_host = ""
target_port = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send("data".encode())

response = client.recv(4096)
print(response)
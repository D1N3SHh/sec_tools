#!/usr/bin/python3

# Just simple TCP server made using 'socket' module.
# This project was created only for learning and will not be developed any more.
# Author: D1N3SHh


import socket, threading

target_host = "0.0.0.0"
target_port = 9999


def handle_client(client):
    request = client.recv(1024)
    print('[!] Received: ', str(request.decode()))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((target_host, target_port))
server.listen(3)
print('[!] Waiting for connection')


while True:

    client, addr = server.accept()
    print('[!] New connection from ', addr[0], ':', addr[1])

    client_handler = threading.Thread(target=handle_client(client))
    client_handler.start()
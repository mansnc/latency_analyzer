from scapy.all import ICMP, IP, IPv6, ICMPv6EchoRequest, sr1, sr # sr1 stands for single packet transmission/reception
from get_IPv6 import get_ipv6_address
import time 

def scapy_measure_latency(addr, count = None, packet_size = None, ttl = None, interval = None, timeout= None, ip_version = None):
    payload = b"A" * packet_size
    latency = []

    for pkt in range(count):
        if ip_version == 4:
            packet = IP(dst = addr, ttl=ttl) / ICMP() / payload
        elif ip_version ==6:
            target_ipv6 = get_ipv6_address(addr)
            if target_ipv6 is not None: # check if domain supports IPv6
                packet = IPv6(dst = target_ipv6, hlim=ttl) / ICMPv6EchoRequest() / payload
            else:
                print(f"{addr} does not support IPv6 at the moment; thus using IPv4 for latency measurement...")
                packet = IP(dst = addr, ttl=ttl) / ICMP() / payload
        t_before_send = time.time() # time stamp before sending 
        #print(packet.show())
        reply = sr1 (packet, timeout = timeout, verbose = 0) # for debug: verbose = 1: will give the status of the packet 
        t_after_reply = time.time() # time stamp after getting response 
        if reply is None:
            latency.append(-1) # I choose "-1" as the codee for no response or packet lost!
        else: 
            latency.append((t_after_reply - t_before_send)*1000) # time in ms
        time.sleep(interval)

    return latency












from module_latency_measurement import measure_latency

addr = "8.8.8.8"
pkts2send = 5
pktsize = 64
ttl = 128
interval = 1
IP_v = 4 # or 6

latency = measure_latency(addr, IP_v, pkts2send, pktsize, ttl, interval)

if latency is not None:
    print(f"Latency to {addr}: {latency} ms")
else:
    print(f"Failed to measure latency to {addr}")

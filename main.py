from module_latency_measurement import measure_latency

ip_addr = "8.8.8.8"
pkts2send = "1"
latency = measure_latency(ip_addr, pkts2send)

if latency is not None:
    print(f"Latency to {ip_addr}: {latency} ms")
else:
    print(f"Failed to measure latency to {ip_addr}")

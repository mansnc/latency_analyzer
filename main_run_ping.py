import statistics
from module_ping_measure_latency import ping_measure_latency

instances = [
    {"addr": "github.com", "pkts2send": 3, "pktsize": 64, "ttl": 128, "interval": 1, "IP_v": 4},
    {"addr": "google.com", "pkts2send": 4, "pktsize": 128, "ttl": 64, "interval": 3, "IP_v": 6},
    {"addr": "bing.com", "pkts2send": 4, "pktsize": 128, "ttl": 64, "interval": 3, "IP_v": 4},
]

results = []

for instance in instances:
    try:
        latency = ping_measure_latency(
            instance["addr"],
            instance["pkts2send"],
            instance["pktsize"],
            instance["ttl"],
            instance["interval"],
            instance["IP_v"]
        )
        results.append({"instance": instance, "latency": latency})
    except Exception as e:
        print(f"Error measuring latency for instance: {instance['addr']}, Error: {e}")

# 'results' contains the latency measurements for each instance
stats = []
for result in results:
    instance = result["instance"]
    latency = result["latency"]
    if latency: 
        stats.append({"instance": instance, "Latency": latency, "Max Latency": max(latency), "Min Latency": min(latency), "Success Ratio": len(latency)/instance['pkts2send']*100, "Mean": statistics.mean(latency)})
        print(f"Instance: {instance['addr']}, Latency-all-pkts: {latency} ms, Max Latency: {max(latency)}, Min Latency: {min(latency)}, Mean Latency: {statistics.mean(latency)}, Success Ratio: {len(latency)/instance['pkts2send']*100}")
    elif not latency:
        print(f"Instance: {instance['addr']} with the given ping config, faild to respond to any of the ICMP requests")


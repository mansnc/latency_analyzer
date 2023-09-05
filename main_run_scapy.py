from module_scapy_measure_latency import scapy_measure_latency

instances = [
{"addr": "bing.com", "pkts2send": 1, "pktsize": 64, "ttl": 64, "interval": 2, "IP_v": 4, "timeout": 1},
{"addr": "github.com", "pkts2send": 1, "pktsize": 64, "ttl": 128, "interval": 1, "IP_v": 4, "timeout": 2},
{"addr": "google.com", "pkts2send": 1, "pktsize": 128, "ttl": 64, "interval": 1, "IP_v": 4, "timeout": 3}
]

results_scapy = []

for instance in instances:
    try:
        latency = scapy_measure_latency(
        instance["addr"],
        instance["pkts2send"],
        instance["pktsize"],
        instance["ttl"],
        instance["interval"], 
        instance["timeout"],
        instance["IP_v"]
    )
        results_scapy.append({"instance": instance, "latency": latency})
        print(f"instance: {instance['addr']}, Latency:  {latency}")
    except Exception as e:
        print(f"Error measuring latency for instance: {instance['addr']}, Error: {e}")

    #print("Done!")
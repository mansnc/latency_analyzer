import json
import os
from module_scapy_measure_latency import scapy_measure_latency
from module_ping_measure_latency import ping_measure_latency
from visualize_results import visualize_results

dir_path = os.path.dirname(os.path.realpath(__file__)) # Get the directory containing the currently running script
json_path = os.path.join(dir_path, 'instances.json') # Build the full path to the JSON file
with open(json_path, 'r') as file:
    instances = json.load(file)

results_scapy = []
results_ping = []
for instance in instances:
    try:
        latency_scapy = scapy_measure_latency(
        instance["addr"],
        instance["pkts2send"],
        instance["pktsize"],
        instance["ttl"],
+        instance["interval"], 
        instance["timeout"],
        instance["IP_v"]
    )
        latency_ping = ping_measure_latency(
        instance["addr"],
        instance["pkts2send"],
        instance["pktsize"],
        instance["ttl"],
        instance["interval"],
        instance["IP_v"]
        )
        results_scapy.append({"addr": instance["addr"], "latency_scapy": latency_scapy})
        results_ping.append({"addr": instance["addr"], "latency_ping": latency_ping})
    except Exception as e:
        print(f"Error measuring latency for instance: {instance['addr']}, Error: {e}")

visualize_results(results_scapy,results_ping)



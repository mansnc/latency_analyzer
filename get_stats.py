import statistics

def get_stats(results_scapy,results_ping):
    stats_scapy = []
    for result in results_scapy:
        instance = result["addr"]
        latency = result["latency_scapy"]
        if latency: 
            stats_scapy.append({"addr": instance, "Max Latency": max(latency), "Min Latency": min(latency), "Success Ratio": len(latency)/len(result['latency_scapy'])*100, "Mean": statistics.mean(latency)})

    stats_ping = []
    for result in results_ping:
        instance = result["addr"]
        latency = result["latency_ping"]
        if latency: 
            stats_ping.append({"addr": instance, "Max Latency": max(latency), "Min Latency": min(latency), "Success Ratio": len(latency)/len(result['latency_ping'])*100, "Mean": statistics.mean(latency)})

    return stats_scapy, stats_ping
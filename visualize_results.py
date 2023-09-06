import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import statistics

def visualize_results(results_scapy,results_ping):
    for result in results_scapy: 
        Packets = [p for p in range(1,len(result['latency_scapy'])+1)]
        plt.plot(Packets, result['latency_scapy'], label = result['addr'], linestyle='--', marker='o', linewidth=2)
    plt.grid(True)
    ax = plt.gca() 
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.legend()
    plt.xlabel('Packet index')
    plt.ylabel('Latency (ms)')
    plt.show()

    ########### 
    stats_scapy = []
    for result in results_scapy:
        instance = result["addr"]
        latency = result["latency_scapy"]
        if latency: 
            stats_scapy.append({"addr": instance, "Max Latency": max(latency), "Min Latency": min(latency), "Success Ratio": len(latency)/len(result['latency_scapy'])*100, "Mean": statistics.mean(latency)})
    
    print(stats_scapy)
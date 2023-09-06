import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns
from get_stats import get_stats
from panda_DataFrame import panda_conversion


def visualize_results(results_scapy,results_ping):
    plt.figure(figsize=(15, 10))
    for result in results_scapy: 
        Packets = [p for p in range(1,len(result['latency_scapy'])+1)]
        plt.plot(Packets, result['latency_scapy'], label = result['addr'], linestyle='--', marker='o', linewidth=2)
    plt.grid(True)
    ax = plt.gca() 
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.legend()
    plt.xlabel('Packet index')
    plt.ylabel('Latency (ms)')
    plt.title('Packet-wise resuls for Scapy')
    plt.show()

    stats_scapy, stats_ping = get_stats(results_scapy,results_ping)
    df = panda_conversion (stats_scapy, stats_ping)
    
    plt.figure(figsize=(15, 10))
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    sns.barplot(data=df, x='addr', y='Max Latency', hue='source', ax=axes[0, 0])
    #axes[0, 0].set_title('Comparison of max latency values')
    axes[0, 0].set_xlabel(''), axes[0, 0].set_ylabel('Max Latency (ms)')
    sns.barplot(data=df, x='addr', y='Min Latency', hue='source', ax=axes[0, 1])
    axes[0, 1].set_xlabel(''), axes[0, 1].set_ylabel('Min Latency (ms)')
    sns.barplot(data=df, x='addr', y='Mean', hue='source', ax=axes[1, 0])
    axes[1, 0].set_xlabel(''), axes[1, 0].set_ylabel('Mean Latency (ms)')
    sns.barplot(data=df, x='addr', y='Success Ratio', hue='source', ax=axes[1, 1])
    axes[1, 1].set_xlabel(''), axes[1, 1].set_ylabel('Success Ratio (%)')
    
    plt.tight_layout()
    plt.show()





    ########### 

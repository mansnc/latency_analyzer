# Latency Analyzer

## Packet-Level latency analysis

This project aim to analyze packet-level latency using combination of python scripting and regular python coding for data processing with two different scenarios: 
- Using standard ping interface and sending ICMP sequences. All processing in this scenario are post-processing. 
- Using **Scapy** library that exploits more sophisticated tools to manipulate the packets and make different types of analysis. This utilization is done based on real-time processing. 

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [CI/CD Environment and Tests](#tests)
    3.1. [Jenkins Setup](#jenkinssetup)
    3.2. [Docker Setup](#dockersetup)


## Features
When basic ping command is used, the main.py will initiate ping commands with the following options given by the user: 

- Number of packets to send 
- IP version (4 or 6)
- Packet Size
- Time to Live (TTL)
- Transmission Interval

User can set different target host address (either IP address or hostname) and all commands and calculations are conducted through one module called "Latency Measurement Module". Both Windows and Linux/MacOS will recognize the input as they are different in terms of the option letters. For instance, number of packets in Unix/MacOS system is determined by switch "-c" while in windows it is determined by "-n". 


```bash
# Clone this repository
git clone https://github.com/mansnc/latency_analyzer.git
```

## Requirements

This project requires the following packages to be installed before running. Assuming "pip" is already installed:  

```
pip install subprocess
pip install platform
pip install statistics
```

## Usage 
Simply go to main.py and modify the section instances based on your need: 

```
instances = [
    {"addr": "github.com", "pkts2send": 3, "pktsize": 64, "ttl": 128, "interval": 1, "IP_v": 4},
    {"addr": "google.com", "pkts2send": 4, "pktsize": 128, "ttl": 64, "interval": 3, "IP_v": 6},
    {"addr": "bing.com", "pkts2send": 4, "pktsize": 128, "ttl": 64, "interval": 3, "IP_v": 4},
    # add more instances here...
]
```

You can add more instances to this data structure as mentioned above. After modifying your instances, simply run the code and see the results. Here is the snapshot of the results: 

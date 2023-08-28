import subprocess
import platform
import re

def measure_latency(ip_addr, pkts2send):
    try:
        if platform.system()=="Windows":
            count_option = "-n"
        else:
            count_option = "-c"
        ping_out = subprocess.check_output(["ping", count_option,pkts2send, ip_addr])
        time = get_round_trip_time (ping_out)
        return time
    except subprocess.CalledProcessError:
        return None
    
def get_round_trip_time(ping_out):
    ping_str = ping_out.decode("utf-8")
    # look for time and extract the number 
    substring1 = "time="
    substring2 = "TTL"
    idx1 = ping_str.find(substring1)
    idx2 = ping_str.find(substring2)
    time_str = ping_str[(idx1 + len(substring1)):idx2]
    time_str = re.sub("ms", "", time_str) 
    
    return int(time_str)





    
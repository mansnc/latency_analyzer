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
        ping_str = ping_out.decode("utf-8")
        #print(ping_str)
        time = get_round_trip_time (ping_str)
        return time
    except subprocess.CalledProcessError:
        return None
    
def get_round_trip_time(ping_str):
    # look for time and extract the number 
    start_sep='time='
    end_sep='ms'
    result=[]
    tmp=ping_str.split(start_sep)
    for par in tmp:
        if end_sep in par:
            result.append(par.split(end_sep)[0])
    #print(result)

    time = []
    for item in result:
        time.append(int(item))
    # print(time)
    
    return time





    
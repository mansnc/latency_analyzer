import subprocess
import platform
import re

def ping_with_options(host, ip_version=None, count=None, packet_size=None, ttl=None, interval=None):
    cmd = ['ping']
    if platform.system()=="Windows":
        count_option = '-n'
        size_option = '-l'
        ttl_option = '-i'
        interwal_option = "-w"
    else:
        count_option = '-c'
        size_option = '-s'
        ttl_option = '-i'
        interwal_option = '-w'

    if ip_version:
        cmd.append('-4' if ip_version == 4 else '-6')

    if count:
        cmd.append(count_option)
        cmd.append(str(count))

    if packet_size:
        cmd.append(size_option)
        cmd.append(str(packet_size))

    if ttl:
        cmd.append(ttl_option)
        cmd.append(str(ttl))

    if interval:
        cmd.append(interwal_option)
        cmd.append(str(interval))

    cmd.append(host)

    try:
        result = subprocess.check_output(cmd, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode}\n{e.output}"

def measure_latency(addr, ip_v, pkts2send, psize, ttl_val, interval_val):
        ping_out = ping_with_options (addr, ip_version = ip_v, count = pkts2send, packet_size = psize, ttl = ttl_val, interval = interval_val)
        #ping_str = ping_out.decode("utf-8")
        print(ping_out)
        time = get_round_trip_time (ping_out)
        return time

    
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







    
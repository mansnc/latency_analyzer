from get_round_trip import get_round_trip_time
from ping_with_options import ping_with_options

def ping_measure_latency(addr, pkts2send, psize, ttl_val, interval_val, ip_v):

# ping_with_options(host, count=None, packet_size=None, ttl=None, timeout=None, ip_version=None)

    ping_out = ping_with_options (addr, count = pkts2send, packet_size = psize, ttl = ttl_val, interval = interval_val, ip_version = ip_v)
    time     = get_round_trip_time (ping_out)
    
    return time





    
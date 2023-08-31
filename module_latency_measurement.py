from get_round_trip import get_round_trip_time
from ping_with_options import ping_with_options


def measure_latency(addr, ip_v, pkts2send, psize, ttl_val, interval_val):

    ping_out = ping_with_options (addr, ip_version = ip_v, count = pkts2send, packet_size = psize, ttl = ttl_val, interval = interval_val)
    time     = get_round_trip_time (ping_out)
    
    return time





    
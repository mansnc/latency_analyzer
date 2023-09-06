import socket

def get_ipv6_address(domain):
    try:
        return socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0] # AF_INET6 indicates that we want an IPv6 address
    except (socket.gaierror, IndexError):
        return None
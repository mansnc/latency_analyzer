import subprocess
import platform


def ping_with_options(host, count=None, packet_size=None, ttl=None, timeout=None, ip_version=None):
    cmd = ['ping']
    if platform.system()=="Windows":
        count_option = '-n'
        size_option = '-l'
        ttl_option = '-i'
        timeout_option = "-w"
    else:
        count_option = '-c'
        size_option = '-s'
        ttl_option = '-i'
        timeout_option = '-W'

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

    if timeout:
        cmd.append(timeout_option)
        cmd.append(str(timeout))

    cmd.append(host)

    try:
        result = subprocess.check_output(cmd, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode}\n{e.output}"
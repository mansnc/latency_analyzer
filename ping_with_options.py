import subprocess
import platform

def is_macos():
    return platform.system() == 'Darwin'
def is_linux():
    return platform.system() == 'Linux'
def is_windows():
    return platform.system() == 'Windows'

def ping_with_options(host, count=None, packet_size=None, ttl=None, interval=None, ip_version=None):
    
    
    if is_windows():
        count_option = '-n'
        size_option = '-l'
        ttl_option = '-i'
        #interval_option = "-w" Not availanle in Windows!
    elif is_macos():
        count_option = '-c'
        size_option = '-s'
        ttl_option = '-t'
        interval_option = '-i'
    elif is_linux():
        count_option = '-c'
        size_option = '-s'
        ttl_option = '-t'
        interval_option = '-i'

    if (is_windows() and ip_version):
        cmd = ['ping']
        cmd.append('-4' if ip_version == 4 else '-6')
        
    elif (is_macos() and ip_version==4):
        cmd = ['ping']
    elif (is_macos() and ip_version==6):
        cmd = ['ping6']

    if count:
        cmd.append(count_option)
        cmd.append(str(count))

    if packet_size:
        cmd.append(size_option)
        cmd.append(str(packet_size))
    
    if is_macos():
        if (ttl and ip_version==4):
            cmd.append(ttl_option)
            cmd.append(str(ttl))
    if not is_macos():
        cmd.append(ttl_option)
        cmd.append(str(ttl))

    if (interval and not is_windows()): #bcuz interval option is not available in windows
        cmd.append(interval_option)
        cmd.append(str(interval))

    cmd.append(host)

    try:
        result = subprocess.check_output(cmd, universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.returncode}\n{e.output}"
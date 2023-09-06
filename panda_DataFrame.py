import pandas as pd

def panda_conversion(results_scapy,results_ping):
    df_scapy = pd.DataFrame(results_scapy)
    df_ping = pd.DataFrame(results_ping)

    df_scapy['source'] = 'results_scapy'
    df_ping['source'] = 'results_ping'

    df = pd.concat([df_scapy, df_ping])

    return df

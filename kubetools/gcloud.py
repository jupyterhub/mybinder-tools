from subprocess import check_output, check_call
import pandas as pd
import re

def get_gcloud_node_info():
    cmd = 'gcloud compute instances list'
    out = check_output(cmd.split())
    lines = out.decode().split('\n')
    lines[0] = lines[0].replace('PREEMPTIBLE', '')
    lines[0] = lines[0].lower()
    lines = [ii.split() for ii in lines]
    df = pd.DataFrame(lines[1:], columns=lines[0])
    return df.dropna()
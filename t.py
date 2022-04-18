import os
import json
import urllib.request
import re
from http.client import RemoteDisconnected, IncompleteRead

BASE_URL = 'https://dns.google/resolve?name='
slp2px_base = 'slp2px-east-std00.oray.net'
slp2px_file = './dns.txt'
slp2px_idx_file = './idx.txt'

slp2p_base = 'slp2p-east-std00.oray.net'
slp2p_file = './dns2.txt'
slp2p_idx_file = './idx2.txt'

def resolve(base, file, idx_file, request_range):
    requested_idxs = []
    if os.path.exists(idx_file):
        with open(idx_file, 'r') as f:
            requested_idxs = f.readlines()
            for i in range(len(requested_idxs)):
                requested_idxs[i] = int(requested_idxs[i].strip())
            f.close()
    if len(requested_idxs) == request_range: return
    with open(file, 'a') as f, open(idx_file, 'a') as idxf:
        for i in range(request_range):
            if i in requested_idxs: continue
            if i < 10: i = '0' + str(i)
            else: i = str(i)
            url = re.sub('00', i, base)
            req_url = BASE_URL + url + '&type=A'
            req = urllib.request.urlopen(req_url)
            page = req.read()
            dict = json.loads(page)
            idxf.write(i)
            idxf.write('\n')
            if 'Answer' in dict:
                f.write(url)
                f.write('\n')
                f.write(dict['Answer'][0]['data'])
                f.write('\n')

cnt = 0
while cnt < 20:
    print(cnt)
    try:
        resolve(slp2px_base, slp2px_file, slp2px_idx_file, 1000)
        resolve(slp2p_base, slp2p_file, slp2p_idx_file, 2000)
    except (ValueError, RemoteDisconnected, IncompleteRead) as e:
        pass
    cnt += 1

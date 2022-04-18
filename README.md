# OrayDns

## Usage
```bash
git clone https://github.com/liyufan/OrayDns
cd OrayDns
cat dns.txt dns2.txt > new.txt
```
## Query IP from scratch
```bash
rm *.txt
python t.py
```
## Work behind a proxy
In `t.py`, specify the proxy address and port
```python
import os
ip: str = 'localhost'
port: int = 8080
os.environ['http_proxy'] = f'http://{ip}:{port}'
os.environ['https_proxy'] = f'http://{ip}:{port}'
```

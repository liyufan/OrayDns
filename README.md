# OrayDns

## Find authoritative nameservers
```
$ dig sl-log.oray.net +trace

; <<>> DiG 9.10.3-P4-Ubuntu <<>> sl-log.oray.net +trace
;; global options: +cmd
.                       86524   IN      NS      m.root-servers.net.
.                       86524   IN      NS      b.root-servers.net.
.                       86524   IN      NS      c.root-servers.net.
.                       86524   IN      NS      d.root-servers.net.
.                       86524   IN      NS      e.root-servers.net.
.                       86524   IN      NS      f.root-servers.net.
.                       86524   IN      NS      g.root-servers.net.
.                       86524   IN      NS      h.root-servers.net.
.                       86524   IN      NS      a.root-servers.net.
.                       86524   IN      NS      i.root-servers.net.
.                       86524   IN      NS      j.root-servers.net.
.                       86524   IN      NS      k.root-servers.net.
.                       86524   IN      NS      l.root-servers.net.
.                       86524   IN      RRSIG   NS 8 0 518400 20220430050000 20220417040000 47671 . QtPd6v9AoPAivRMVCxWLh/DgJpzpr9SAhaEccnZjTPtqWljvX1+67b7P 3aAeiQA9oddjtS6AslfnWhl/7zrMhDLANUUt9BWohud22+NoItjeUWUF c9V2xToQZUQ0zawx/PZYNy9uVfTrzWmYH9y5/gIHqapWathaxY+ycO4N Ezu0PeK7Jms70iTAocnUqCdqopnS5QeaWrz7t96k/EyYrJHKYHAA8ua3 QvxXUjYNenoIWiS3Od6R9Ta1XsNCOlXw99kW27WotlY9j4fMyccwuCv+ 6jEmwRNP1W5gD12fyCGUJLaCY39L3MVLoekOYIDbEhB0VGLIsnEzVdfk 4hHxiQ==
;; Received 525 bytes from 8.8.8.8#53(8.8.8.8) in 189 ms

net.                    172800  IN      NS      d.gtld-servers.net.
net.                    172800  IN      NS      b.gtld-servers.net.
net.                    172800  IN      NS      c.gtld-servers.net.
net.                    172800  IN      NS      f.gtld-servers.net.
net.                    172800  IN      NS      i.gtld-servers.net.
net.                    172800  IN      NS      m.gtld-servers.net.
net.                    172800  IN      NS      j.gtld-servers.net.
net.                    172800  IN      NS      g.gtld-servers.net.
net.                    172800  IN      NS      a.gtld-servers.net.
net.                    172800  IN      NS      l.gtld-servers.net.
net.                    172800  IN      NS      k.gtld-servers.net.
net.                    172800  IN      NS      e.gtld-servers.net.
net.                    172800  IN      NS      h.gtld-servers.net.
net.                    86400   IN      DS      35886 8 2 7862B27F5F516EBE19680444D4CE5E762981931842C465F00236401D 8BD973EE
net.                    86400   IN      RRSIG   DS 8 1 86400 20220429170000 20220416160000 47671 . BhzJBw/Nbnm7I21OwyrMjD3LHM7Pj5IXn/nmK6/2fDnGiBuJ8Emjb/Za smksqQr+CNVVlGYaG6ZR0L8Bz5GQgj6917N8moEdkfZsnkff3A5olXHv wQcl5MyLoUXFQhU6cdiXL2kcN6pwUmq3tluzyLbIsSYGnh8WUDtV+J5R 68kPTGw5wJ8lciWFKIsR+rtNz9kmef3ZcAukizhOaorSVSvFFwG/mtr0 Y7uEymPZosuYXNb0btLBzJc9wLIIhSs38YGPeEMI5ISjPx8nu8HaGwDP wpcNOp02qp/eBh9I6+GtqFT3Rc5fWPIE+eehseUxgXEK6i7OyQ/qNS/j z9dBpQ==
;; Received 1172 bytes from 193.0.14.129#53(k.root-servers.net) in 41 ms

oray.net.               172800  IN      NS      ns1.oray.com.
oray.net.               172800  IN      NS      ns2.oray.com.
A1RT98BS5QGC9NFI51S9HCI47ULJG6JH.net. 86400 IN NSEC3 1 1 0 - A1RTLNPGULOGN7B9A62SHJE1U3TTP8DR NS SOA RRSIG DNSKEY NSEC3PARAM
A1RT98BS5QGC9NFI51S9HCI47ULJG6JH.net. 86400 IN RRSIG NSEC3 8 2 86400 20220421055929 20220414044929 4604 net. s0zPQkEZbam0ir4Y0tcwBFvZpm7XYYpjecGIP31F2qQUQAfA/NpraS2b KPQbS4YXXiDXO+heGF2H1tTV+tEidxhh6221LISMCpYwy4d88X5BN3SV dAxwKz4IRdNsJJChJS2YjFdU4ql0DN/Gmk3fKorIeIOHuQYB/RHS2M0R c3QrHOFz0TXOX3o9IshQlfzjy8YswWxpZvPoHjDHvkjPkw==
37CTFEJ08H6TS1GKLA4TH171TMRHH2OK.net. 86400 IN NSEC3 1 1 0 - 37CVC6341LUSRCHAEATHEDNOQP7FBHCG NS DS RRSIG
37CTFEJ08H6TS1GKLA4TH171TMRHH2OK.net. 86400 IN RRSIG NSEC3 8 2 86400 20220423055533 20220416044533 45728 net. BysmenlIegUBJV2r6IhatcR6nI/8spBV5BPOGB0of5FejZguCFJeLzJS +EArFiGsbr2MWYBgmiYI7m+DgheXAawPdlBpdqW68t3CtoxeUkve06zc 9ajBgKwl+VAYRZ4LKwue0KyZzZ6ivHzaXRdP7kfIPPmEmDX0Y7ESyJcF 1p3rC5BiERO7nItHq6o2iFQiPrRznPqy0jYog42lkex5BA==
;; Received 637 bytes from 192.35.51.30#53(f.gtld-servers.net) in 220 ms

sl-log.oray.net.        60      IN      A       120.26.160.74
sl-log.oray.net.        60      IN      A       121.40.118.44
sl-log.oray.net.        60      IN      A       121.199.72.21
sl-log.oray.net.        60      IN      A       121.41.32.171
;; Received 140 bytes from 106.75.14.38#53(ns2.oray.com) in 27 ms

```

## `sl-tk.oray.com`
```
$ dig @ns1.oray.com sl-tk.oray.com +short
121.40.242.11
116.62.45.157
120.26.124.112
120.26.107.6
112.124.20.98
101.37.116.112
116.62.101.24
121.40.63.86
$ dig @ns2.oray.com sl-tk.oray.com +short
121.40.242.11
116.62.45.157
112.124.20.98
120.26.124.112
116.62.101.24
121.40.63.86
120.26.107.6
101.37.116.112
```
## `sl-log.oray.net`
```
$ dig @ns1.oray.com sl-log.oray.net +short
121.41.32.171
121.40.118.44
120.26.160.74
121.199.72.21
$ dig @ns2.oray.com sl-log.oray.net +short
121.199.72.21
121.40.118.44
120.26.160.74
121.41.32.171
```
## Others
```
$ dig @ns1.oray.com slp2px-east-std50.oray.net +short
180.97.153.133
$ dig @ns2.oray.com slp2px-east-std50.oray.net +short
180.97.153.133
$ dig @ns1.oray.com slp2px-east-std47.oray.net +short
180.97.156.90
$ dig @ns2.oray.com slp2px-east-std47.oray.net +short
180.97.156.90
$ dig @ns1.oray.com slp2px-east-std07.oray.net +short
180.97.153.211
$ dig @ns2.oray.com slp2px-east-std07.oray.net +short
180.97.153.211
$ dig @ns1.oray.com slp2p-east-std148.oray.net +short
180.113.2.130
$ dig @ns2.oray.com slp2p-east-std148.oray.net +short
180.113.2.130
```

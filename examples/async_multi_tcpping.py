"""
    tcppinglib  -   Easy Way to Measure the Connectivity and Latency
    
    :copyright: Copyright 2021-2024 Engin EKEN.
    :license: GNU LGPLv3, see the LICENSE for details. 

    ----------------------------------------------------------------

    Examples for async_multi_tcpping
"""
from tcppinglib import async_multi_tcpping
import asyncio

urls = [
    # FQDNs
    'https://www.google.com/',
    'https://www.hepsiburada.com/', 
    'cnn.com', 

    # IP Addresses
    '1.1.1.1'
    ]

hosts = asyncio.run(async_multi_tcpping(urls, count=5, interval=1.5))

for host in hosts:
    print(host.is_alive, host.avg_rtt_all)

# True 226.72
# True 62.649
# True 93.685
# True 9.165
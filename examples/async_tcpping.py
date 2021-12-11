"""
    tcppinglib  -   Easy Way to Measure the Connectivity and Latency
    
    :copyright: Copyright 2021-2024 Engin EKEN.
    :license: GNU LGPLv3, see the LICENSE for details. 

    ----------------------------------------------------------------

    Examples for async_tcpping
"""

from tcppinglib import async_tcpping
import asyncio

async def host_specs(address):
    host = await async_tcpping(address, count=5, interval=1.5)
    print(host.avg_rtt_all, host.is_alive)

asyncio.run(host_specs('https://www.google.com/'))
# 215.261 True
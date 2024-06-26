"""
    tcppinglib  -   Easy Way to Measure the Connectivity and Latency
    
    :copyright: Copyright 2021-2024 Engin EKEN.
    :license: GNU LGPLv3, see the LICENSE for details. 

    ----------------------------------------------------------------

    Examples for async_tcpping
"""

import asyncio

from tcppinglib import async_tcpping


async def host_specs(address):
    host = await async_tcpping(address, count=7, interval=1.5)
    print(host.avg_rtt, host.is_alive)

asyncio.run(host_specs('https://www.google.com'))
# 215.261 True
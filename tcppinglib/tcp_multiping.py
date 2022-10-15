"""
    tcppinglib
    ~~~~~~~
    
    Monitor your endpoints with TCP Ping.

        https://github.com/EnginEken/tcppinglib
    
    :copyright: Copyright 2021-2026 Engin EKEN.
    :license: GNU LGPLv3, see the LICENSE for details.
    
    ~~~~~~~
    
    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public License
    as published by the Free Software Foundation, either version 3 of
    the License, or (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.
    You should have received a copy of the GNU Lesser General Public
    License along with this program.  If not, see
    <https://www.gnu.org/licenses/>.
"""

import asyncio
from .tcp_ping import async_tcpping


async def async_multi_tcpping(
    addresses: list,
    port: int = 80,
    timeout: float = 2,
    count: int = 5,
    interval: float = 3,
    concurrent_tasks=50,
):
    loop = asyncio.get_running_loop()
    tasks = []
    tasks_pending = set()
    for address in addresses:
        if len(tasks_pending) >= concurrent_tasks:
            _, tasks_pending = await asyncio.wait(
                tasks_pending, return_when=asyncio.FIRST_COMPLETED
            )
        task = loop.create_task(async_tcpping(address, port, timeout, count, interval))
        tasks.append(task)
        tasks_pending.add(task)
    await asyncio.wait(tasks_pending)
    return [task.result() for task in tasks]


def multi_tcpping(
    addresses: list,
    port: int = 80,
    timeout: float = 2,
    count: int = 5,
    interval: float = 3,
    concurrent_tasks=50,
):
    return asyncio.run(
        async_multi_tcpping(
            addresses=addresses,
            port=port,
            timeout=timeout,
            count=count,
            interval=interval,
            concurrent_tasks=concurrent_tasks,
        )
    )

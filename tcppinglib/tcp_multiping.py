import asyncio
from .tcp_ping import async_tcpping

async def async_multi_tcpping(addresses: list, port: int = 443, timeout: float = 2, count: int = 3, interval: float = 3, concurrent_tasks=50, ipv6: bool = False):
    loop = asyncio.get_running_loop()
    tasks = []
    tasks_pending = set()
    for address in addresses:
        if len(tasks_pending) >= concurrent_tasks:
             _, tasks_pending = await asyncio.wait(tasks_pending, return_when=asyncio.FIRST_COMPLETED)
        task = loop.create_task(async_tcpping(address, port, timeout, count, interval, ipv6))
        tasks.append(task)
        tasks_pending.add(task)
    await asyncio.wait(tasks_pending)
    return [task.result() for task in tasks]


def multi_tcpping(addresses: list, port: int = 443, timeout: float = 2, count: int = 3, interval: float = 3, concurrent_tasks=50, ipv6: bool = False):
    return asyncio.run(
        async_multi_tcpping(
            addresses=addresses,
            port=port,
            timeout=timeout,
            count=count,
            interval=interval,
            concurrent_tasks=concurrent_tasks,
            ipv6=ipv6
        ))


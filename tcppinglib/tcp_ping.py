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

import socket
import time
import asyncio

from .models import *
from .tcp_sockets import *
from .utils import *


def tcpping(
    address: str,
    port: int = 80,
    timeout: float = 2,
    count: int = 5,
    interval: float = 3,
):

    address = strip_http_https(address)

    if is_hostname(address):
        address = hostname_lookup(address, port, socket.AF_INET)[0]

    if is_ipv6(address):
        _Socket = TCPv6Socket
    else:
        _Socket = TCPv4Socket

    packets_sent = 0
    rtts = []

    for sequence in range(count):
        with _Socket() as sock:
            if sequence > 0:
                time.sleep(interval)

            request = TCPRequest(destination=address, port=port, timeout=timeout)

            try:
                sock.connect(request)
                packets_sent += 1
                rtts.append(request.time)

            except Exception as e:
                print(e)

    return TCPHost(address, port, packets_sent, count - packets_sent, rtts)


async def async_tcpping(
    address: str,
    port: int = 80,
    timeout: float = 2,
    count: int = 5,
    interval: float = 3,
):

    address = strip_http_https(address)

    if is_hostname(address):
        address = (await async_hostname_lookup(address, port, socket.AF_INET))[0]

    if is_ipv6(address):
        _Socket = TCPv6Socket
    else:
        _Socket = TCPv4Socket

    packets_sent = 0
    rtts = []

    for sequence in range(count):
        with AsyncTCPSocket(_Socket()) as sock:
            if sequence > 0:
                await asyncio.sleep(interval)
            
            request = TCPRequest(destination=address, port=port, timeout=timeout)

            try:
                await sock.connect(request)
                packets_sent += 1
                rtts.append(request.time)

            except Exception as e:
                print(e)

    return TCPHost(address, port, packets_sent, count - packets_sent, rtts)

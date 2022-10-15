'''
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
'''

import asyncio
import socket
from re import match, sub

from .exceptions import *


def hostname_lookup(hostname, port, family):
    """
    Resolve a hostname or FQDN to an IP address. This function is resolving hostnames based on
    your configured DNS in your system. Several IP addresses may return. In that case, first resolved
    IP address will be used.

    :type hostname: str
    :param hostname: Hostname or FQDN

    :type port: int
    :param port: Port number of the destination system

    :type family: socket family
    :param family: socket.AF_INET for v4, socket.AF_INET6 for v6
    """
    try:
        host_ip = socket.getaddrinfo(
            host=hostname, port=port, family=family, proto=socket.IPPROTO_TCP
        )
        return [resolved_ip[4][0] for resolved_ip in host_ip]

    except socket.gaierror:
        raise NameLookupError(hostname)


async def async_hostname_lookup(hostname, port, family):
    """
    Resolve a hostname or FQDN to an IP address asyncronously. This function is resolving hostnames based on
    your configured DNS in your system. Several IP addresses may return. In that case, first resolved
    IP address will be used.

    This function is non-blocking.

    :type hostname: str
    :param hostname: Hostname or FQDN

    :type port: int
    :param port: Port number of the destination system

    :type family: socket family
    :param family: socket.AF_INET for v4, socket.AF_INET6 for v6
    """
    loop = asyncio.get_running_loop()

    try:
        host_ip = await loop.getaddrinfo(
            host=hostname, port=port, family=family, proto=socket.IPPROTO_TCP
        )
        return [resolved_ip[4][0] for resolved_ip in host_ip]

    except socket.gaierror:
        raise NameLookupError(hostname)


def is_hostname(name):
    """
    Indicate whether the specified name is a hostname or an FQDN.
    Return a `boolean`.
    """
    pattern = r"(?i)^([a-z0-9-]+|([a-z0-9_-]+[.])+[a-z]+)$"
    return match(pattern, name) is not None


def is_ipv6(ip):
    """
    Indicate whether the ip address is IPv6 address.
    Return a `boolean`.
    """
    pattern = r"^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$"
    return match(pattern, ip) is not None


def strip_http_https(name):
    """
    Stripping `http://` and `https://` from hostname if there is.
    Return a `string`
    """
    return sub(r"^(http|https)?:\/\/", "", name)

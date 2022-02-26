import asyncio
import socket

from re import match
from urllib.parse import urlparse

from .exceptions import *


def is_ipv4(ip):
    pattern = r'^([0-9]{1,3}[.]){3}[0-9]{1,3}$'
    return match(pattern, ip) is not None

def is_ipv6(ip):
    pattern = r'^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$'
    return match(pattern, ip) is not None

def url_parse(address):
    is_https = False
    parsed_url = urlparse(address)
    if address.startswith('http:') or address.startswith('https:'):
        address = parsed_url.hostname
        port = parsed_url.port
        if parsed_url.scheme == 'https':
            is_https = True
        if not port:
            if parsed_url.scheme == 'https':
                port = 443
            else:
                port = 80
        path = parsed_url.path
    else:
        args = address.split('/', 1)
        address = args[0]
        try:
            path = (args[1:])[0]
        except IndexError:
            path = ''
        try:
            port = int(address.split(':')[1])
            address = address.split(':')[0]
            if port == 443:
                is_https = True
        except IndexError:
            port = 80

    return address, port, path, is_https



async def async_hostname_lookup(hostname, port, family):
    loop = asyncio.get_running_loop()
    try:
        host_ip = await loop.getaddrinfo(host=hostname, port=port, family=family, proto=socket.IPPROTO_TCP)
        return [resolved_ip[4][0] for resolved_ip in host_ip]
    except socket.gaierror:
        raise NameLookupError(hostname)

def hostname_lookup(hostname, port, family):
    try:
        host_ip = socket.getaddrinfo(host=hostname, port=port, family=family, proto=socket.IPPROTO_TCP)
        return [resolved_ip[4][0] for resolved_ip in host_ip]
    except socket.gaierror:
        raise NameLookupError(hostname)
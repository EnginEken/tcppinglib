# TCPPINGLIB

<div align="center">
  <br>
  <br>
  <img src="media/TcpPingLib.png" height="340" width="817" alt="icmplib">
  <br>
  <br>
</div>

<br>


When it comes to measuring the connectivity and latency to web servers on the network level, an alternative method exists, which we call TCP Ping: a ping with special options that mimic the TCP handshake that takes place when an HTTP/HTTPS connection is established.

***TCPPingLib*** is a TCP oriented ping alternative written in pure Python. It is used to test the reachability of a service on a host using TCP/IP and measure the time it takes to connect to the specifed port.

It is not only measuring connection overall time to the web server, but also measuring every steps between start point of a tcpping and connection which are dns lookup time, socket connection time, SSL socket connection time if possible and it also send basic HTTP GET request for the response and measure the response time.


## Features

- :love_you_gesture: **No Dependency:** TcpPingLib is a pure Python implementation of TCP Ping. It has no external dependency.
- :mechanical_leg: **IPv6 Support:** You can use TcpPingLib with the URLs with IPv6 address. You can also see the all resolved IP addresses for the specified address.
- :rocket: **Fast:** Developed for best and fastest performance with async functions like `async_tcpping`, `async_multi_tcpping`.
- :fire: **Built-in Properties:** Easily get the necessary information with the built-in models' properties about the TCP Ping which is sent.
- :eyes: **Monitor:** Determine whether the host is online or not whenever `ping` is disabled or blocked, measure the latency, check if SSL connection can be done.
- :hourglass: **Certificate Expire:** Check the days to certification expire date for the given URL if SSL connection can be established.
- :gem: **Modern:** This library uses the latest mechanisms offered by Python 3.6/3.7+ and is fully object-oriented.

## Installation

- Recommended way to install `tcppinglib` is to use `pip3`

    ```shell
    $ pip3 install tcppinglib
    ```
    > Python 3.7 or later is required to use the library.

## Usage

### ***tcpping***
- Send TCP Ping to a URL.
- Import the function with the below code snippet.

```python
from tcppinglib import tcpping
```

#### Function Parameters

```python
tcpping(address, port: int = 443, timeout: float = 2, count: int = 3, interval: float = 3, ipv6: bool = False)
```

- `address`

    The hostname or FQDN of the host which tcp ping will be sent to.

    - Type: `str`

- `count`

    The number of packets which will be sent to `address`.

    - Type: `int`
    - Default: `3`

- `port`

    The TCP port number that packets will be sent to.

    - Type: `int`
    - Default: `443`(HTTPS)

- `timeout`

    The maximum waiting time for receiving a reply in seconds.

    - Type: `float`
    - Default: `2` seconds

- `interval`

    The interval between sending each packet in seconds

    - Type: `float`
    - Default: `3` seconds

- `ipv6`

    Selection if you want to try resolving and sending tcp ping packets for ipv6 address of the URL.

    - Type: `bool`
    - Default: `False`

#### Return Value

- A `TcpHost` object will be returned containing with many usefull values about the TCP Ping. <br>
`ip_address`, `port`, `ssl_version`, `req_resp`, `cert_expire`, `packets_sent`, `packets_received`, `packet_loss`, `is_alive`, `min_rtt_all`, `avg_rtt_all`, `max_rtt_all`, `min_rtt_dns`, `avg_rtt_dns`, `max_rtt_dns`, `min_rtt_conn`, `avg_rtt_conn`, `max_rtt_conn`, `min_rtt_sslconn`, `avg_rtt_sslconn`, `max_rtt_sslconn`, `min_rtt_req`, `avg_rtt_req`, `max_rtt_req`

#### Example

```python
>>> from tcppinglib import tcpping

>>> host = tcpping('www.google.com:80', count=5, interval=1.5)

>>> host.is_alive           # Check whether host is responding
True

>>> host.ip_address         # Resolved ip addresses of the given url
['172.217.17.100']

>>> host.min_rtt_all        # Minimum round trip time for all process
15.532

>>> host.avg_rtt_dns        # Average round trip time for dns resolution
3.575

>>> host.avg_rtt_all        # Average round trip time for all process
18.789

>>> host.packet_loss        # Percentage of packet loss
0.0

>>> host.ssl_version        # SSL Version, it cant get the ssl version because the port number is 80
'Cant Get SSL Version'

>>> host.port               # Port number 
80
```
<br>

### ***multi_tcpping***

- Send TCP Ping to multiple URL.
- Import the function with the below code snippet.

```python
from tcppinglib import multi_tcpping
```

#### Function Parameters

```python
multi_tcpping(addresses: list, port: int = 443, timeout: float = 2, count: int = 3, interval: float = 3, concurrent_tasks=50, ipv6: bool = False):
```

- `address`

    The hostname or FQDN of the host which tcp ping will be sent to.

    - Type: `str`

- `count`

    The number of packets which will be sent to `address`.

    - Type: `int`
    - Default: `3`

- `port`

    The TCP port number that packets will be sent to.

    - Type: `int`
    - Default: `443`(HTTPS)

- `timeout`

    The maximum waiting time for receiving a reply in seconds.

    - Type: `float`
    - Default: `2` seconds

- `interval`

    The interval between sending each packet in seconds

    - Type: `float`
    - Default: `3` seconds

- `concurrent_tasks`

    The maximum number of concurrent tasks to speed up processing. This value cannot exceed the maximum number of file descriptors configured on the operating system.

    - Type: `int`
    - Default: `50`

- `ipv6`

    Selection if you want to try resolving and sending tcp ping packets for ipv6 address of the URL.

    - Type: `bool`
    - Default: `False`

#### Return Value

- A `TcpHost` object will be returned containing with many usefull values about the TCP Ping. <br>
`ip_address`, `port`, `ssl_version`, `req_resp`, `cert_expire`, `packets_sent`, `packets_received`, `packet_loss`, `is_alive`, `min_rtt_all`, `avg_rtt_all`, `max_rtt_all`, `min_rtt_dns`, `avg_rtt_dns`, `max_rtt_dns`, `min_rtt_conn`, `avg_rtt_conn`, `max_rtt_conn`, `min_rtt_sslconn`, `avg_rtt_sslconn`, `max_rtt_sslconn`, `min_rtt_req`, `avg_rtt_req`, `max_rtt_req`

#### Example

```python
>>> from tcppinglib import multi_tcpping

>>> hosts = multi_tcpping(['www.google.com:80', 'https://www.python.org/', 'http://cnn.com'], count=5, interval=1.5, concurrent_tasks=20)

>>> [host.is_alive for host in hosts]                               # Check whether hosts are responding respectively
[True, True, True]

>>> [host.avg_rtt_all for host in hosts]                            # Averate round trip times list for whole process.
[88.602, 279.328, 131.029]

>>> [host.ssl_version for host in hosts]                            # SSL Version, it cant get the ssl version if the port number is 80
['Cant Get SSL Version', 'TLSv1.3', 'Cant Get SSL Version']

>>> [host.ip_address for host in hosts]                             # Resolved ip addresses list
[['172.217.169.100'], ['151.101.12.223'], ['151.101.193.67', '151.101.65.67', '151.101.1.67', '151.101.129.67']]

>>> [host.port for host in hosts]                                   # Port Number
[80, 443, 80]
```

<br>

### ***async_tcpping***

- Send TCP Ping to a URL.
- This function is non-blocking.
- Import the function with the below code snippet.

```python
from tcppinglib import async_tcpping
```

#### Function Parameters

```python
async_tcpping(address, port: int = 443, timeout: float = 2, count: int = 3, interval: float = 3, ipv6: bool = False)
```

- `address`

    The hostname or FQDN of the host which tcp ping will be sent to.

    - Type: `str`

- `count`

    The number of packets which will be sent to `address`.

    - Type: `int`
    - Default: `3`

- `port`

    The TCP port number that packets will be sent to.

    - Type: `int`
    - Default: `443`(HTTPS)

- `timeout`

    The maximum waiting time for receiving a reply in seconds.

    - Type: `float`
    - Default: `2` seconds

- `interval`

    The interval between sending each packet in seconds

    - Type: `float`
    - Default: `3` seconds

- `ipv6`

    Selection if you want to try resolving and sending tcp ping packets for ipv6 address of the URL.

    - Type: `bool`
    - Default: `False`

#### Return Value

- A `TcpHost` object will be returned containing with many usefull values about the TCP Ping. <br>
`ip_address`, `port`, `ssl_version`, `req_resp`, `cert_expire`, `packets_sent`, `packets_received`, `packet_loss`, `is_alive`, `min_rtt_all`, `avg_rtt_all`, `max_rtt_all`, `min_rtt_dns`, `avg_rtt_dns`, `max_rtt_dns`, `min_rtt_conn`, `avg_rtt_conn`, `max_rtt_conn`, `min_rtt_sslconn`, `avg_rtt_sslconn`, `max_rtt_sslconn`, `min_rtt_req`, `avg_rtt_req`, `max_rtt_req`

#### Example

```python
>>> import asyncio
>>> from tcppinglib import async_tcpping

>>> async def host_specs(address):
...     host = await async_tcpping(address, count=5, interval=1.5)
...     return host.is_alive, host.avg_rtt_all, host.packet_loss
... 

>>> asyncio.run(host_specs('https://www.google.com/'))
(True, 450.629, 0.0)
```
<br>

### ***async_multi_tcpping***

- Send TCP Ping to multiple URL.
- This function is non-blocking.
- Import the function with the below code snippet.

```python
from tcppinglib import async_multi_tcpping
```

#### Function Parameters

```python
async_multi_tcpping(address, port: int = 443, timeout: float = 2, count: int = 3, interval: float = 3, concurrent_tasks=50, ipv6: bool = False)
```

- `address`

    The hostname or FQDN of the host which tcp ping will be sent to.

    - Type: `str`

- `count`

    The number of packets which will be sent to `address`.

    - Type: `int`
    - Default: `3`

- `port`

    The TCP port number that packets will be sent to.

    - Type: `int`
    - Default: `443`(HTTPS)

- `timeout`

    The maximum waiting time for receiving a reply in seconds.

    - Type: `float`
    - Default: `2` seconds

- `interval`

    The interval between sending each packet in seconds

    - Type: `float`
    - Default: `3` seconds

- `concurrent_tasks`

    The maximum number of concurrent tasks to speed up processing. This value cannot exceed the maximum number of file descriptors configured on the operating system.

    - Type: `int`
    - Default: `50`

- `ipv6`

    Selection if you want to try resolving and sending tcp ping packets for ipv6 address of the URL.

    - Type: `bool`
    - Default: `False`

#### Return Value

- A `TcpHost` object will be returned containing with many usefull values about the TCP Ping. <br>
`ip_address`, `port`, `ssl_version`, `req_resp`, `cert_expire`, `packets_sent`, `packets_received`, `packet_loss`, `is_alive`, `min_rtt_all`, `avg_rtt_all`, `max_rtt_all`, `min_rtt_dns`, `avg_rtt_dns`, `max_rtt_dns`, `min_rtt_conn`, `avg_rtt_conn`, `max_rtt_conn`, `min_rtt_sslconn`, `avg_rtt_sslconn`, `max_rtt_sslconn`, `min_rtt_req`, `avg_rtt_req`, `max_rtt_req`

#### Example

```python
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
```

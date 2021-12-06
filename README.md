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

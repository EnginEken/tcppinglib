"""
    tcppinglib  -   Easy Way to Measure the Connectivity and Latency
    
    :copyright: Copyright 2021-2024 Engin EKEN.
    :license: GNU LGPLv3, see the LICENSE for details. 

    ----------------------------------------------------------------

    Examples for multi_tcpping
"""

from tcppinglib import multi_tcpping

hosts = multi_tcpping(['https://www.google.com/', 'http://cnn.com', 'www.python.org:443'], count=5, interval=1.5, ipv6=True) # IPv6 address resolution

for host in hosts:
    print(host)

#   www.google.com - ::ffff:172.217.169.100
# ------------------------------------------------------------
#   Packets sent:                    5
#   Packets received:                5
#   Packet lost:                     0
#   Packet loss:                     0.0%
#   Overall Round-trip times:        225.093 ms / 231.98 ms / 249.058 ms
#   DNS Round-trip times:            1.662 ms / 8.052 ms / 33.093 ms
#   Connection Round-trip times:     14.594 ms / 18.772 ms / 21.749 ms
#   SSL Round-trip times:            83.273 ms / 85.246 ms / 86.711 ms
#   Request Round-trip times:        110.245 ms / 118.826 ms / 124.176 ms
# ------------------------------------------------------------
#   cnn.com - ::ffff:151.101.129.67
# ------------------------------------------------------------
#   Packets sent:                    5
#   Packets received:                5
#   Packet lost:                     0
#   Packet loss:                     0.0%
#   Overall Round-trip times:        156.232 ms / 214.811 ms / 426.994 ms
#   DNS Round-trip times:            119.31 ms / 178.857 ms / 388.194 ms
#   Connection Round-trip times:     32.274 ms / 35.937 ms / 38.781 ms
#   SSL Round-trip times:            0.0 ms / 0.0 ms / 0.0 ms
#   Request Round-trip times:        0.0 ms / 0.0 ms / 0.0 ms
# ------------------------------------------------------------
#   www.python.org - ::ffff:199.232.16.223
# ------------------------------------------------------------
#   Packets sent:                    5
#   Packets received:                5
#   Packet lost:                     0
#   Packet loss:                     0.0%
#   Overall Round-trip times:        119.124 ms / 178.133 ms / 387.641 ms
#   DNS Round-trip times:            1.536 ms / 50.837 ms / 245.843 ms
#   Connection Round-trip times:     30.057 ms / 34.569 ms / 41.542 ms
#   SSL Round-trip times:            82.35 ms / 92.556 ms / 101.657 ms
#   Request Round-trip times:        0.0 ms / 0.0 ms / 0.0 ms
# ------------------------------------------------------------


# Also all the TcpHost Class properties can be accessible for multi_tcpping

for host in hosts:
    print(f'{host._address}:  {host.is_alive}')
    print(f'{host._address}:  {host.ssl_version}')
    print(f'{host._address}:  {host.avg_rtt_all}')

# www.google.com:  True
# www.google.com:  TLSv1.3
# www.google.com:  282.135
# cnn.com:  True
# cnn.com:  Cant Get SSL Version
# cnn.com:  48.048
# www.python.org:  True
# www.python.org:  TLSv1.3
# www.python.org:  221.998
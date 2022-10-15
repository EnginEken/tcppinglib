"""
    tcppinglib  -   Easy Way to Measure the Connectivity and Latency
    
    :copyright: Copyright 2021-2024 Engin EKEN.
    :license: GNU LGPLv3, see the LICENSE for details. 

    ----------------------------------------------------------------

    Examples for multi_tcpping
"""

from tcppinglib import multi_tcpping

hosts = multi_tcpping(
    ["https://www.google.com/", "http://cnn.com", "www.python.org"],
    count=10,
    interval=1.5,
)

for host in hosts:
    print(host)

#   142.250.187.174
# ------------------------------------------------------------
#   Packets sent:                    10
#   Packets received:                10
#   Packet lost:                     0
#   Packet loss:                     0.0%
#   Overall Round-trip times:        225.093 ms / 231.98 ms / 249.058 ms
#   min/avg/max Round-trip times:    1.662 ms / 8.052 ms / 33.093 ms
# ------------------------------------------------------------
#   151.101.67.5
# ------------------------------------------------------------
#   Packets sent:                    10
#   Packets received:                10
#   Packet lost:                     0
#   Packet loss:                     0.0%
#   min/avg/max Round-trip times:    156.232 ms / 214.811 ms / 426.994 ms
# ------------------------------------------------------------
#   138.197.63.241
# ------------------------------------------------------------
#   Packets sent:                    10
#   Packets received:                10
#   Packet lost:                     0
#   Packet loss:                     0.0%
#   min/avg/max Round-trip times:    119.124 ms / 178.133 ms / 387.641 ms
# ------------------------------------------------------------


# Also all the TcpHost Class properties can be accessible for multi_tcpping

for host in hosts:
    print(f"{host.ip_address}:  {host.is_alive}")

# 142.250.187.174:  True
# 151.101.67.5:  True
# 138.197.63.241:  True

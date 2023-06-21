"""
    tcppinglib  -   Easy Way to Measure the Connectivity and Latency
    
    :copyright: Copyright 2021-2024 Engin EKEN.
    :license: GNU LGPLv3, see the LICENSE for details. 

    ----------------------------------------------------------------

    Examples for tcpping
"""

from tcppinglib import tcpping

host = tcpping(
    "https://www.google.com", port=443, count=10, interval=1.5
)  # IPv4 address resolution

# Sending tcpping to google.


print(f"IP Address: {host.ip_address}")  # IP Address: '216.58.206.164'

print(f"Port Number: {host.port}")  # Port Number: 443

print(f"Is_alive: {host.is_alive}")  # Is_alive: True

print(f"Number of packets sent: {host.packets_sent}")  # Number of packets sent: 10

print(
    f"Number of packets received: {host.packets_received}"
)  # Number of packets received: 10


# RTTs


print(
    f"overall_min: {host.min_rtt}, overall_avg: {host.avg_rtt}, overall_max: {host.max_rtt},  overall_stddev: {host.stddev_rtt}"
)
# overall_min: 215.57, overall_avg: 270.47, overall_max: 700.475, overall_stddev: 143.454

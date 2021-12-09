"""
    tcppinglib  -   Easy Way to Measure the Connectivity and Latency
    
    :copyright: Copyright 2021-2024 Engin EKEN.
    :license: GNU LGPLv3, see the LICENSE for details. 

    ----------------------------------------------------------------

    Examples for tcpping
"""

from tcppinglib import tcpping

host1 = tcpping('https://www.google.com/', count=5, interval=1.5, ipv6=True) # IPv6 address resolution

host2 = tcpping('https://www.google.com/', count=10, interval=1.5) # IPv4 address resolution

# Sending tcpping to google. Address, port and path will be automatically parsed based on given URL. See url_parse example.


print(f'IPv6 Address: {host1.ip_address}')                          # IPv6 Address: ['::ffff:216.58.206.164']
print(f'IP Address: {host2.ip_address}')                            # IP Address: ['216.58.206.164']

print(f'Port Number: {host1.port}')                                 # Port Number: 443
print(f'Port Number: {host2.port}')                                 # Port Number: 443

print(f'Is_alive: {host1.is_alive}')                                # Is_alive: True
print(f'Is_alive: {host2.is_alive}')                                # Is_alive: True

print(f'SSL Version: {host1.ssl_version}')                          # SSL Version: TLSv1.3
print(f'SSL Version: {host2.ssl_version}')                          # SSL Version: TLSv1.3

print(f'HTTP Response Code: {host1.req_resp}')                      # HTTP Response Code: 200
print(f'HTTP Response Code: {host2.req_resp}')                      # HTTP Response Code: 200

print(f'Days to Ceritficate Expiration: {host1.cert_expire}')       # Days to Ceritficate Expiration: 52
print(f'Days to Ceritficate Expiration: {host2.cert_expire}')       # Days to Ceritficate Expiration: 52

print(f'Number of packets sent: {host1.packets_sent}')              # Number of packets sent: 5
print(f'Number of packets sent: {host2.packets_sent}')              # Number of packets sent: 10

print(f'Number of packets received: {host1.packets_received}')      # Number of packets received: 5
print(f'Number of packets received: {host2.packets_received}')      # Number of packets received: 10


# RTTs 

print(f'overall_min_ipv6: {host1.min_rtt_all}, overall_avg_ipv6: {host1.avg_rtt_all}, overall_max_ipv6: {host1.max_rtt_all}')
# overall_min_ipv6: 214.703, overall_avg_ipv6: 228.983, overall_max_ipv6: 255.587

print(f'overall_min: {host2.min_rtt_all}, overall_avg: {host2.avg_rtt_all}, overall_max: {host2.max_rtt_all}')
# overall_min: 215.57, overall_avg: 270.47, overall_max: 700.475

print(f'dnslookup_min_ipv6: {host1.min_rtt_dns}, dnslookup_avg: {host1.avg_rtt_dns}, dnslookup_max: {host1.max_rtt_dns}')
# dnslookup_min_ipv6: 0.662, dnslookup_avg: 3.999, dnslookup_max: 14.782

print(f'dnslookup_min: {host2.min_rtt_dns}, dnslookup_avg: {host2.avg_rtt_dns}, dnslookup_max: {host2.max_rtt_dns}')
# dnslookup_min: 0.492, dnslookup_avg: 0.933, dnslookup_max: 1.058

print(f'connection_time_min_ipv6: {host1.min_rtt_conn}, connection_time_avg_ipv6: {host1.avg_rtt_conn}, connection_time_max_ipv6: {host1.max_rtt_conn}')
# connection_time_min_ipv6: 13.461, connection_time_avg_ipv6: 14.576, connection_time_max_ipv6: 15.389

print(f'connection_time_min: {host2.min_rtt_conn}, connection_time_avg: {host2.avg_rtt_conn}, connection_time_max: {host2.max_rtt_conn}')
# connection_time_min: 13.899, connection_time_avg: 18.167, connection_time_max: 28.765

print(f'SSLConnection_time_min_ipv6: {host1.min_rtt_sslconn}, SSLConnection_time_avg_ipv6: {host1.avg_rtt_sslconn}, SSLConnection_time_max_ipv6: {host1.max_rtt_sslconn}')
# SSLConnection_time_min_ipv6: 79.896, SSLConnection_time_avg_ipv6: 83.583, SSLConnection_time_max_ipv6: 86.912

print(f'SSLConnection_time_min: {host2.min_rtt_sslconn}, SSLConnection_time_avg: {host2.avg_rtt_sslconn}, SSLConnection_time_max: {host2.max_rtt_sslconn}')
# SSLConnection_time_min: 81.624, SSLConnection_time_avg: 85.579, SSLConnection_time_max: 92.174

print(f'request_time_min_ipv6: {host1.min_rtt_req}, request_time_avg_ipv6: {host1.avg_rtt_req}, request_time_max_ipv6: {host1.max_rtt_req}')
# request_time_min_ipv6: 115.249, request_time_avg_ipv6: 125.723, request_time_max_ipv6: 157.34

print(f'request_time_min: {host2.min_rtt_req}, request_time_avg: {host2.avg_rtt_req}, request_time_max: {host2.max_rtt_req}')
# request_time_min: 110.983, request_time_avg: 165.616, request_time_max: 597.529
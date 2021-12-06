import asyncio
import time
import ssl
import socket
import warnings
import datetime

from time import sleep
from .utils import *
from .exceptions import *
from .models import *

async def async_tcpping(address, port: int = 443, timeout: float = 2, count: int = 3, interval: float = 3, ipv6: bool = False):
    
    address, port, path, is_https = url_parse(address)
    
    start_times, rtt_times = dict(), dict()
    cipher = 'DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256'
    packet_lost, packets_sent = 0, 0
    is_certified = False
    ssl_version = ''
    daysToExpiration = 0
    path_response_code = ''
    rtt_times['all'], rtt_times['dns_lookup'], rtt_times['connection'], rtt_times['ssl_conn'], rtt_times['get_req'] = [], [], [], [], []  
    

    for lap in range(count):
        if lap > 0:
            await asyncio.sleep(interval)
        
        try:
            start_times['all'] = time.perf_counter()
            # Dns lookup section
      
            start_times['dns_lookup'] = time.perf_counter()
            if ipv6:
                resolved_ips = await async_hostname_lookup(address, port, socket.AF_INET6)
                hostip = resolved_ips[0]
            else:
                resolved_ips = await async_hostname_lookup(address, port, socket.AF_INET)
                hostip = resolved_ips[0]
            rtt_times['dns_lookup'].append(time.perf_counter() - start_times['dns_lookup'])

            # Check if ip address is v4 or v6. Later this info will be used for socket type
            ip_type = is_ipv4(hostip)    

            # IPv4 or IPv6 SocketConnection
            start_times['connection'] = time.perf_counter()
            network_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) if ip_type else socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            network_sock.settimeout(timeout)
            connection = network_sock.connect_ex((hostip, int(port)))
            
            if connection != 0:
                raise PortNotOpenError(port, address)
            else:
                rtt_times['connection'].append(time.perf_counter() - start_times['connection'])
                    
            # SSL Conenction and CertExpire Time
            if is_https:
                start_times['ssl_conn'] = time.perf_counter()
                try:
                    context = ssl.create_default_context()
                    context.set_ciphers(cipher)
                    sock = socket.create_connection((hostip, port))
                    ssock = context.wrap_socket(sock, server_hostname = address)
                    
                    rtt_times['ssl_conn'].append(time.perf_counter() - start_times['ssl_conn'])
                    
                    ssl_version = ssock.version()

                    certificate = ssock.getpeercert()
                    certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    daysToExpiration = (certExpires - datetime.datetime.now()).days
                    
                    is_certified = True

                except ssl.SSLError:
                    warnings.warn(SslConnectionError(port, address))
                    network_sock = ssl.wrap_socket(network_sock)
                    rtt_times['ssl_conn'].append(time.perf_counter() - start_times['ssl_conn'])
                    ssl_version = network_sock.version()
                    pass
            
            # GET Request if there is path in address(url)
            if path:
                start_times['get_req'] = time.perf_counter()
                if not is_certified:
                    network_sock.send("GET {0} HTTP/1.0\r\nHost: {1}\r\n\r\n".format(path, address).encode('ascii'))
                    data = network_sock.recv()
                    data = data.decode('ascii', errors='ignore')
                    try:
                        path_response_code = int(data.split('\n')[0].split()[1])
                    except:
                        pass
                    rtt_times['get_req'].append(time.perf_counter() - start_times['get_req'])
                else:
                    ssock.send("GET {0} HTTP/1.0\r\nHost: {1}\r\n\r\n".format(path, address).encode('ascii'))
                    data = ssock.recv()
                    data = data.decode('ascii', errors='ignore')
                    try:
                        path_response_code = int(data.split('\n')[0].split()[1])
                    except:
                        pass
                    rtt_times['get_req'].append(time.perf_counter() - start_times['get_req'])
            
            rtt_times['all'].append(time.perf_counter() - start_times['all'])
            
            
            network_sock.close()
            try:
                ssock.close()
            except UnboundLocalError:
                pass
        except:
            packet_lost += 1
            pass
        
        count -= 1
        packets_sent += 1
        
            
    return TcpHost(address, port, packets_sent, packet_lost, rtt_times, ssl_version, path_response_code, daysToExpiration, resolved_ips)




def tcpping(address, port: int = 443, timeout: float = 2, count: int = 3, interval: float = 3, ipv6: bool = False):
    
    address, port, path, is_https = url_parse(address)
    
    start_times, rtt_times = dict(), dict()
    cipher = 'DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA:ECDHE-ECDSA-AES128-GCM-SHA256'
    packet_lost, packets_sent = 0, 0
    is_certified = False
    ssl_version = ''
    daysToExpiration = 0
    path_response_code = ''
    rtt_times['all'], rtt_times['dns_lookup'], rtt_times['connection'], rtt_times['ssl_conn'], rtt_times['get_req'] = [], [], [], [], []  
    

    for lap in range(count):
        if lap > 0:
            sleep(interval)
        
        try:
            start_times['all'] = time.perf_counter()
            
            # Dns lookup section
            start_times['dns_lookup'] = time.perf_counter()
            if ipv6:
                resolved_ips = hostname_lookup(address, port, socket.AF_INET6)
                hostip = resolved_ips[0]
            else:
                resolved_ips = hostname_lookup(address, port, socket.AF_INET)
                hostip = resolved_ips[0]
            rtt_times['dns_lookup'].append(time.perf_counter() - start_times['dns_lookup'])

            # Check if ip address is v4 or v6. Later this info will be used for socket type
            ip_type = is_ipv4(hostip)    

            # IPv4 or IPv6 SocketConnection
            start_times['connection'] = time.perf_counter()
            network_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) if ip_type else socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            network_sock.settimeout(timeout)
            connection = network_sock.connect_ex((hostip, int(port)))
            
            if connection != 0:
                raise PortNotOpenError(port, address)
            else:
                rtt_times['connection'].append(time.perf_counter() - start_times['connection'])
                    
            # SSL Conenction and CertExpire Time 
            if is_https:
                start_times['ssl_conn'] = time.perf_counter()
                try:
                    context = ssl.create_default_context()
                    context.set_ciphers(cipher)
                    sock = socket.create_connection((hostip, port))
                    ssock = context.wrap_socket(sock, server_hostname = address)
                    
                    rtt_times['ssl_conn'].append(time.perf_counter() - start_times['ssl_conn'])
                    
                    ssl_version = ssock.version()

                    certificate = ssock.getpeercert()
                    certExpires = datetime.datetime.strptime(certificate['notAfter'], '%b %d %H:%M:%S %Y %Z')
                    daysToExpiration = (certExpires - datetime.datetime.now()).days
                    
                    is_certified = True

                except ssl.SSLError:
                    warnings.warn(SslConnectionError(port, address))
                    network_sock = ssl.wrap_socket(network_sock)
                    rtt_times['ssl_conn'].append(time.perf_counter() - start_times['ssl_conn'])
                    ssl_version = network_sock.version()
                    pass
            
            # GET Request if there is path in address(url)
            if path:
                start_times['get_req'] = time.perf_counter()
                if not is_certified:
                    network_sock.send("GET {0} HTTP/1.0\r\nHost: {1}\r\n\r\n".format(path, address).encode('ascii'))
                    data = network_sock.recv()
                    data = data.decode('ascii', errors='ignore')
                    try:
                        path_response_code = int(data.split('\n')[0].split()[1])
                    except:
                        pass
                    rtt_times['get_req'].append(time.perf_counter() - start_times['get_req'])
                else:
                    ssock.send("GET {0} HTTP/1.0\r\nHost: {1}\r\n\r\n".format(path, address).encode('ascii'))
                    data = ssock.recv()
                    data = data.decode('ascii', errors='ignore')
                    try:
                        path_response_code = int(data.split('\n')[0].split()[1])
                    except:
                        pass
                    rtt_times['get_req'].append(time.perf_counter() - start_times['get_req'])
            
            rtt_times['all'].append(time.perf_counter() - start_times['all'])
            
            
            network_sock.close()
            try:
                ssock.close()
            except UnboundLocalError:
                pass
        except:
            packet_lost += 1
            pass
        
        count -= 1
        packets_sent += 1
        
            
    return TcpHost(address, port, packets_sent, packet_lost, rtt_times, ssl_version, path_response_code, daysToExpiration, resolved_ips)
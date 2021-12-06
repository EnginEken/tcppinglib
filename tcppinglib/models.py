from .exceptions import *

class TcpHost:
    def __init__(self, address, port, packets_sent, packet_lost, rtts, ssl_version, path_response_code, daysToExpiration, resolved_ips):
        self._address = address
        self._port = port
        self._packets_sent = packets_sent
        self._packet_lost = packet_lost
        self._rtts = rtts
        self._ssl_version= ssl_version
        self._path_response_code = path_response_code
        self._daysToExpiration = daysToExpiration
        self._resolved_ips = resolved_ips

    
    def __repr__(self):
        return f'<Host [{self._address}]>'

    def __str__(self):
        return f'  {self._address} - {self._resolved_ips[0]}\n' + '-' * 60 + '\n' \
               f'  Packets sent:                    {self._packets_sent}\n' \
               f'  Packets received:                {self.packets_received}\n' \
               f'  Packet lost:                     {self._packet_lost}\n' \
               f'  Packet loss:                     {self.packet_loss}%\n' \
               f'  Overall Round-trip times:        {self.min_rtt_all} ms / {self.avg_rtt_all} ms / {self.max_rtt_all} ms\n' \
               f'  DNS Round-trip times:            {self.min_rtt_dns} ms / {self.avg_rtt_dns} ms / {self.max_rtt_dns} ms\n' \
               f'  Connection Round-trip times:     {self.min_rtt_conn} ms / {self.avg_rtt_conn} ms / {self.max_rtt_conn} ms\n' \
               f'  SSL Round-trip times:            {self.min_rtt_sslconn} ms / {self.avg_rtt_sslconn} ms / {self.max_rtt_sslconn} ms\n' \
               f'  Request Round-trip times:        {self.min_rtt_req} ms / {self.avg_rtt_req} ms / {self.max_rtt_req} ms\n' + '-' * 60

    @property
    def port(self):
        return self._port

    @property
    def ip_address(self):
        return self._resolved_ips
    
    @property
    def ssl_version(self):
        return self._ssl_version if self._ssl_version else 'Cant Get SSL Version'
    
    @property
    def req_resp(self):
        return self._path_response_code if self._path_response_code else 'Cant Sent GET Request'
    
    @property
    def cert_expire(self):
        if self._daysToExpiration != 0:
            return self._daysToExpiration
        else:
            raise SslConnectionError(self._address)

    @property
    def packets_sent(self):
        return self._packets_sent

    @property
    def packets_received(self):
        return len(self._rtts['all'])

    @property
    def packet_loss(self):
        if not self._packets_sent:
            return 0.0

        return round((self._packet_lost / self._packets_sent) * 100, 2)
    
    @property
    def is_alive(self):
        return len(self._rtts) > 0

    @property
    def min_rtt_all(self):
        if not self._rtts['all']:
            return 0.0

        return round(min(self._rtts['all']) * 1000, 3)
    
    @property
    def avg_rtt_all(self):
        if not self._rtts['all']:
            return 0.0

        return round((sum(self._rtts['all']) / len(self._rtts['all'])) * 1000, 3)

    @property
    def max_rtt_all(self):
        if not self._rtts['all']:
            return 0.0

        return round(max(self._rtts['all']) * 1000, 3)

    @property
    def min_rtt_dns(self):
        if not self._rtts['dns_lookup']:
            return 0.0

        return round(min(self._rtts['dns_lookup']) * 1000, 3)
    
    @property
    def avg_rtt_dns(self):
        if not self._rtts['dns_lookup']:
            return 0.0

        return round((sum(self._rtts['dns_lookup']) / len(self._rtts['dns_lookup'])) * 1000, 3)

    @property
    def max_rtt_dns(self):
        if not self._rtts['dns_lookup']:
            return 0.0

        return round(max(self._rtts['dns_lookup']) * 1000, 3)

    @property
    def min_rtt_conn(self):
        if not self._rtts['connection']:
            return 0.0

        return round(min(self._rtts['connection']) * 1000, 3)
    
    @property
    def avg_rtt_conn(self):
        if not self._rtts['connection']:
            return 0.0

        return round((sum(self._rtts['connection']) / len(self._rtts['connection'])) * 1000, 3)

    @property
    def max_rtt_conn(self):
        if not self._rtts['connection']:
            return 0.0

        return round(max(self._rtts['connection']) * 1000, 3)
    
    @property
    def min_rtt_sslconn(self):
        if not self._rtts['ssl_conn']:
            return 0.0

        return round(min(self._rtts['ssl_conn']) * 1000, 3)
    
    @property
    def avg_rtt_sslconn(self):
        if not self._rtts['ssl_conn']:
            return 0.0

        return round((sum(self._rtts['ssl_conn']) / len(self._rtts['ssl_conn'])) * 1000, 3)

    @property
    def max_rtt_sslconn(self):
        if not self._rtts['ssl_conn']:
            return 0.0

        return round(max(self._rtts['ssl_conn']) * 1000, 3)
    
    @property
    def min_rtt_req(self):
        if not self._rtts['get_req']:
            return 0.0

        return round(min(self._rtts['get_req']) * 1000, 3)
    
    @property
    def avg_rtt_req(self):
        if not self._rtts['get_req']:
            return 0.0

        return round((sum(self._rtts['get_req']) / len(self._rtts['get_req'])) * 1000, 3)

    @property
    def max_rtt_req(self):
        if not self._rtts['get_req']:
            return 0.0

        return round(max(self._rtts['get_req']) * 1000, 3)
    
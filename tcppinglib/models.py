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

class TCPRequest:
    """
    Object that represents a TCP reuqest making 3way handshake.

    :type destination: str
    :param destination: The IP address of the host to which the 3way
    handshake will be performed.

    :type port: int
    :param port: Port number of the destination ip address to which the 3way
    handshake will be performed. Default to 80.

    :type timeout: int
    :param timeout: Value that system will wait to complete 3way handshake
    with the remote destination:port to try again in seconds. Default to 2 secs.
    """

    def __init__(self, destination, port=80, timeout=2) -> None:
        self._destination = destination
        self._port = port
        self._time = 0
        self._timeout = timeout

    def __repr__(self):
        return f"<TCPRequest [{self._destination}]>"

    @property
    def destination(self):
        """
        The IP address of the host to which the 3way
        handshake will be performed.
        """
        return self._destination

    @property
    def port(self):
        """
        Port number of the destination ip address to which the 3way
        handshake will be performed. Default to 80.
        """
        return self._port

    @property
    def timeout(self):
        """
        Value that system will wait to complete 3way handshake
        with the remote destination:port to try again in seconds. Default to 2 secs.
        """
        return self._timeout

    @property
    def time(self):
        """
        The timestamp of the TCP connection.
        Initialized to zero when creating the connection.
        """
        return self._time


class TCPHost:
    """
    The class that represents single TCP host. It has property methods for
    simplified call for the TCP connection results.

    :type destination: str
    :param destination: The IP address of the host to which the 3way
    handshake will be performed.

    :type port: int
    :param port: Port number of the destination ip address to which the 3way
    handshake will be performed.

    :type packets_sent: int
    :param packets_sent: The number of 3-way handshake connection tried to the
    destination host.

    :type packet_lost: int
    :param packet_lost: The number of failed 3-way handshake connection tried
    to the destination host.

    :type rtts: list[float]
    :param rtts: The list of successfull connection times expressed in milliseconds.
    """

    def __init__(self, destination, port, packets_sent, packet_lost, rtts):
        self._destination = destination
        self._port = port
        self._packets_sent = packets_sent
        self._packet_lost = packet_lost
        self._rtts = rtts

    def __repr__(self):
        return f"<Host [{self._destination}]>"

    def __str__(self):
        return (
            f"-" * 60 + "\n"
            f"  {self._destination}\n" + "-" * 60 + "\n"
            f"  Packets sent:                    {self._packets_sent}\n"
            f"  Packets received:                {self.packets_received}\n"
            f"  Packet lost:                     {self._packet_lost}\n"
            f"  Packet loss:                     {self.packet_loss}%\n"
            f"  min/avg/max Round-trip times:    {self.min_rtt} ms / {self.avg_rtt} ms / {self.max_rtt} ms\n"
            + "-" * 60
        )

    @property
    def port(self):
        """
        Port number of the destination ip address to which the 3way
        handshake will be performed.
        """
        return self._port

    @property
    def ip_address(self):
        """
        The IP address of the host to which the 3way
        handshake will be performed.
        """
        return self._destination

    @property
    def packets_sent(self):
        """
        The number of 3-way handshake connection tried to the
        destination host.
        """
        return self._packets_sent

    @property
    def packets_received(self):
        """
        The number of successfull 3-way handshake connection to the
        destination host.
        """
        return len(self._rtts)

    @property
    def packet_loss(self):
        """
        Percentage of successfully completed 3-way handshake based on
        given count.
        """
        if not self._packets_sent:
            return 0.0

        return round((self._packet_lost / self._packets_sent) * 100, 2)

    @property
    def is_alive(self):
        """
        Indicate whether the host is reachable.
        Return a `boolean`.
        """
        return len(self._rtts) > 0

    @property
    def min_rtt(self):
        """
        The minimum successfull connection time in milliseconds.
        """
        if not self._rtts:
            return 0.0

        return round(min(self._rtts) * 1000, 3)

    @property
    def avg_rtt(self):
        """
        The average successfull connection time in milliseconds.
        """
        if not self._rtts:
            return 0.0

        return round((sum(self._rtts) / len(self._rtts)) * 1000, 3)

    @property
    def max_rtt(self):
        """
        The maximum successfull connection time in milliseconds.
        """
        if not self._rtts:
            return 0.0

        return round(max(self._rtts) * 1000, 3)

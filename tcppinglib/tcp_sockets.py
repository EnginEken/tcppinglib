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

import socket
import time

from .exceptions import *


class TCPSocket:
    """
    Base class for TCP sockets
    """

    def __init__(self) -> None:

        self._sock = None
        try:
            self._sock = self._create_socket(
                type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP
            )
        except OSError as err:
            raise err

    def __enter__(self):
        """
        Return this object.
        """
        return self

    def __exit__(self, type, value, traceback):
        """
        Call the `close` method.
        """
        self.close()

    def __del__(self):
        """
        Call the `close` method.
        """
        self.close()

    def _create_socket(self):
        """
        Create new socket. Must be overridden by proper socket class.
        """
        raise NotImplementedError

    def _set_timeout(self):
        """
        Set the timeout for this socket. Must be overridden by proper socket class.
        """
        raise NotImplementedError

    def connect(self, request):
        """
        With this function the port scanner tries to complete a full
        TCP three-way handshake ([SYN], [SYN ACK], [ACK]) with the
        targeted port on the system.

        Be informed that this function is not calculate the packet round-trip time.
        It is calculating the 3-way handshake time which is enough for TCP session
        with the destination system.

        This operation is non-blocking.

        :type request: TCPRequest
        :param request: The TCP request object that have been created.
        """

        if not self._sock:
            raise NotImplementedError

        try:
            sock_port = int(request.port)

            self._set_timeout(request.timeout)
            start_time = time.perf_counter()

            self._sock.connect((request.destination, sock_port))

            request._time = time.perf_counter() - start_time

        except socket.timeout:
            raise PortNotOpenError(sock_port, request.destination)

        except OSError as err:
            if err.errno == 8:
                raise NameLookupError(request.destination)

            raise TCPSocketError(str(err))

    def close(self):
        """
        Close the socket. It cannot be used after this call.
        """
        if self._sock:
            self._sock.close()
            self._sock = None

    @property
    def sock(self):
        """
        Return the underlying socket (`socket.socket` object) or `None`
        if the socket is closed.
        """
        return self._sock

    @property
    def blocking(self):
        """
        Indicate whether the socket is in blocking mode.
        Return a `boolean`.
        """
        return self._sock.getblocking()

    @blocking.setter
    def blocking(self, enable):
        return self._sock.setblocking(enable)

    @property
    def is_closed(self):
        """
        Indicate whether the socket is closed.
        Return a `boolean`.
        """
        return self._sock is None


class TCPv4Socket(TCPSocket):
    """
    Class for creating TCPv4 socket.
    """

    def _create_socket(self, type, proto):
        """
        Create and return new socket.
        """
        return socket.socket(family=socket.AF_INET, type=type, proto=proto)

    def _set_timeout(self, timeout):
        """
        Set the timeout value for created socket.
        """
        self._sock.settimeout(timeout)


class TCPv6Socket(TCPSocket):
    """
    Class for creating TCPv6 socket.
    """

    def _create_socket(self, type, proto):
        """
        Create and return new socket.
        """
        return socket.socket(family=socket.AF_INET6, type=type, proto=proto)

    def _set_timeout(self, timeout):
        """
        Set the timeout value for created socket.
        """
        self._sock.settimeout(timeout)


class AsyncTCPSocket:
    """
    Class for creating sockets asyncronously.

    :type tcp_sock: TCPSocket
    :param tcp_socket: TCP Socket. Once the wrapper is instantiated,
    this socket should no longer be used directly.
    """

    def __init__(self, tcp_sock) -> None:
        self._tcp_sock = tcp_sock
        self._tcp_sock.blocking = False

    def __enter__(self):
        """
        Return this object.
        """
        return self

    def __exit__(self, type, value, traceback):
        """
        Call the `close` method.
        """
        self.close()

    def __del__(self):
        """
        Call the `close` method.
        """
        self.close()

    async def connect(self, request):
        """
        With this function the port scanner tries to complete a full
        TCP three-way handshake ([SYN], [SYN ACK], [ACK]) with the
        targeted port on the system asyncronously.

        This operation is non-blocking.

        Be informed that this function is not calculate the packet round-trip time.
        It is calculating the 3-way handshake time which is enough for TCP session
        with the destination system.

        :type request: TCPRequest
        :param request: The TCP request object that have been created.
        """
        if not self._tcp_sock:
            raise NotImplementedError

        try:
            self._tcp_sock._set_timeout(request.timeout)
            start_time = time.perf_counter()

            self._tcp_sock.connect(request)

            request._time = time.perf_counter() - start_time

        except socket.timeout:
            raise PortNotOpenError(request.port, request.destination)

        except OSError as err:
            if err.errno == 8:
                raise NameLookupError(request.destination)

            raise TCPSocketError(str(err))

    def close(self):
        """
        Close the socket. It cannot be used after this call.
        """
        if self._tcp_sock:
            self._tcp_sock.close()
            self._tcp_sock = None

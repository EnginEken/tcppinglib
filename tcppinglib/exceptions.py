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

class TCPPingLibError(Exception):
    """
    Exception class for the tcppinglib package.
    """


class NameLookupError(TCPPingLibError):
    """
    Raised when the requested name does not exist or cannot be resolved.
    This concerns both Fully Qualified Domain Names and hostnames.
    """

    def __init__(self, address):
        message = f"Given hostname '{address}' cannot be resolved"
        super().__init__(message)


class TCPSocketError(TCPPingLibError):
    """
    Base class for ICMP sockets exceptions.
    """


class PortNotOpenError(TCPPingLibError):
    """
    Raised when the port is not open for the given host.
    """

    def __init__(self, port, address) -> None:
        message = f"The port '{port}' is not open for the host '{address}'!"
        super().__init__(message)

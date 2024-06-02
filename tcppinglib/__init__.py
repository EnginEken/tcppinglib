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

from .exceptions import *
from .models import TCPHost, TCPRequest
from .tcp_multiping import async_multi_tcpping, multi_tcpping
from .tcp_ping import async_tcpping, tcpping
from .utils import (async_hostname_lookup, hostname_lookup, is_hostname,
                    is_ipv6, strip_http_https)

__author__    = 'Engin EKEN'
__copyright__ = 'Copyright 2021-2026 Engin EKEN'
__license__   = 'GNU Lesser General Public License v3.0'

__version__   = '2.0.3'
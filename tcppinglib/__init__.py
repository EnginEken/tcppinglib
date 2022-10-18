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
from .tcp_ping import tcpping, async_tcpping
from .tcp_multiping import multi_tcpping, async_multi_tcpping
from .models import TCPHost, TCPRequest
from .utils import is_hostname, is_ipv6, strip_http_https
from .utils import hostname_lookup, async_hostname_lookup


__author__    = 'Engin EKEN'
__copyright__ = 'Copyright 2021-2026 Engin EKEN'
__license__   = 'GNU Lesser General Public License v3.0'

__version__   = '2.0.3'
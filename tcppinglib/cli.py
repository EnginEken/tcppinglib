"""
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
"""

import argparse
import sys

from .tcp_ping import async_tcpping, tcpping
from .utils import extract_cli_address_and_port, strip_http_https


def parse_arguments():
    """
    Parse command-line arguments using argparse.
    """
    parser = argparse.ArgumentParser(
        description="TCP Ping: An Easy Way to Measure the Connectivity and Latency with TCP Ping"
    )

    parser.add_argument(
        "address",
        type=str,
        help="The IP address or FQDN of the host to ping. You can also specify the port using <ip_address>:<port> format.",
    )

    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=80,
        help="The port number to connect to (default: 80). This will be overridden if a port is specified in the address.",
    )

    parser.add_argument(
        "-t",
        "--timeout",
        type=float,
        default=1,
        help="Timeout in seconds for each ping (default: 1).",
    )

    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=5,
        help="Number of ping requests to send (default: 5).",
    )

    parser.add_argument(
        "-i",
        "--interval",
        type=float,
        default=1,
        help="Interval in seconds between each ping request (default: 1).",
    )

    return parser.parse_args()


def main():
    """
    Main function to handle command-line execution.
    """
    args = parse_arguments()

    try:
        # Extract IP address and port if provided in the <address>:<port> format
        if ":" in args.address:
            address, port = extract_cli_address_and_port(args.address)
        else:
            address = args.address
            port = args.port

        # Run the synchronous TCP ping
        print(
            f"TCPPING {address}:{port}: Sending {args.count} packet{'s' if args.count != 1 else ''}..."
        )
        host = tcpping(
            address=address,
            port=port,
            timeout=args.timeout,
            count=args.count,
            interval=args.interval,
            is_cli=True,
        )
        print(host)

    except ValueError as e:
        print(f"Error: Invalid port value provided.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

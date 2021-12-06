class TcppingLibError(Exception):
    '''
    Base Exception Class
    '''

class NameLookupError(TcppingLibError):
    def __init__(self, address) -> None:
        message = f'The hostname \'{address}\' cannot be resolved!'
        super().__init__(message)

class PortNotOpenError(TcppingLibError):
    def __init__(self, port, address) -> None:
        message = f'The port \'{port}\' is not open for the host \'{address}\'!'
        super().__init__(message)

class SslConnectionError(TcppingLibError):
    def __init__(self, address) -> None:
        message = f'The SSL connection cannot be established for \'{address}\'! But socket connection for this address can be established'
        super().__init__(message)
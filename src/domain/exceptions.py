class MarketIdFormatError(Exception):
    """The format of market id is wrong"""
    pass
class ExchangeApiError(Exception):
    """The call to exchange fail"""
    pass
from src.domain.exceptions import MarketIdFormatError
class MarketId:
    """
    A class used to represent a currency pair object(btc-clp)

    ...

    Attributes
    ----------
    pair : array
        2 elements with the 2 currencies["BTC", "CLP"]

    Methods
    -------
    __normalizeMarket()
        transform and validate the pair currency(BTC-CLP) to ["BTC","CLP"]
    """
    def __init__(self, market_id):

        self.pair = self.__normalizeMarket(market_id)

    def __normalizeMarket(self, market_id):
        """
        Parameters
        ----------
        market_id : str
            currency pair for instance("BTC-CLP")
        """
        if (market_id.find('-') != -1):
            return market_id.split("-")
        else:
            raise MarketIdFormatError;

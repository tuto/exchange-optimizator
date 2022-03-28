from src.domain.exceptions import MarketIdFormatError
class MarketId:
    def __init__(self, market_id):

        self.pair = self.__normalizeMarket(market_id)

    def __normalizeMarket(self, market_id):
        if (market_id.find('-') != -1):
            return market_id.split("-")
        else:
            raise MarketIdFormatError;


    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
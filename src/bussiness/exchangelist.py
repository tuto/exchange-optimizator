from src.domain.marketid import MarketId
import importlib

class ExchangeList:

    def __init__(self):

        self.exchanges = []

    def add(self, exchangeName, additionalParams={}):
        exchangeClass = self.__import(exchangeName)
        exchangeClass.setAdditionalParams(additionalParams)
        self.exchanges.append(exchangeClass)

    def get_minimun_ticker(self, market_id):

        marketId = MarketId(market_id)
        results = []
        for exchange in self.exchanges:
            tickerExchange = exchange.get_ticker(marketId)
            results.append({"name":exchange.get_name(), "price": tickerExchange.last_price})

        return sorted(results, key=lambda ticker: ticker["price"][0])
        
    def __import(self, exchangeName):
        mod = __import__(f'src.repositories.{exchangeName}', fromlist=[exchangeName.capitalize()])
        klass = getattr(mod, exchangeName.capitalize())
        return klass()
    
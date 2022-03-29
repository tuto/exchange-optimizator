from src.domain.marketid import MarketId
import importlib

class ExchangeList:

    def __init__(self):

        self.exchanges = []

    def add(self, exchangeName, additionalParams={}):
        exchangeClass = self.__import(exchangeName)
        exchangeClass.setAdditionalParams(additionalParams)
        self.exchanges.append(exchangeClass)

    def get_prices(self, market_id):

        marketId = MarketId(market_id)
        results = []
        for exchange in self.exchanges:
            tickerExchange = exchange.get_ticker(marketId)
            results.append({"name":exchange.get_name(), "price": tickerExchange.last_price})

        return results

    def order_prices(self, exchanges):
         return sorted(exchanges, key=lambda ticker: ticker["price"][0], reverse=True)

    def calculateCurrencyRate(self, currencyQuantity, exchanges):
        results = []
        for exchange in exchanges:
            quantity = currencyQuantity/exchange["price"][0]
            results.append({exchange["name"]: quantity})
        return results
    def __import(self, exchangeName):
        mod = __import__(f'src.repositories.{exchangeName}', fromlist=[exchangeName.capitalize()])
        klass = getattr(mod, exchangeName.capitalize())
        return klass()
    
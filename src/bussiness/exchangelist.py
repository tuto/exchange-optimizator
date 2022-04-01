from src.domain.marketid import MarketId
from src.bussiness.exchange import Exchange
from src.domain.exceptions import ExchangeApiError

import importlib

class ExchangeList:
    """
    A class used to represent a list of Exchanges
    ...

    Attributes
    ----------
    exchanges : array
        a list of exchanges

    Methods
    -------
    add()
       add exchange to list and import the infrastructure class
    get_prices(market_id)
        get the ticker object from the exchange, 
        with rate and the usd conversion applied
    order_prices(exchanges)
        order exchange list sorted for price
    calculateCurrencyRate(currencyQuantity, market_id)
        calculate the value in cryptocurrency for a quantity of another currency
    __importClient(exchangeName)
        import dinamically a infrastructure client class   
    """
    def __init__(self):

        self.exchanges = []

    def add(self, exchangeName, additionalParams={}):
        """
        Parameters
        ----------
        exchangeName : str
            exchange name
        additionalParams : dict
            a list of additional params for a client
        """
        clientClass = self.__importClient(exchangeName)
        self.exchanges.append(Exchange(exchangeName, additionalParams, clientClass))

    def get_prices(self, market_id) -> list:
        """
        Parameters
        ----------
        market_id : str
            market pair example(btc-clp)
        """
        marketId = MarketId(market_id)
        results = []
        for exchange in self.exchanges:
            try: 
                tickerExchange = exchange.get_ticker(marketId)
                results.append({"name":exchange.get_name(), "price": tickerExchange.last_price})
            except ExchangeApiError as e:
                print(f'Exchange {exchange.get_name()} api raise a exception', e)

        return results

    def order_prices(self, exchanges) -> list:
        """
        Parameters
        ----------
        exchanges : array
            array of exchanges with prices
        """
        return sorted(exchanges, key=lambda ticker: ticker["price"][0], reverse=True)

    def calculateCurrencyRate(self, currencyQuantity, market_id) -> list:
        """
        Parameters
        ----------
        currencyQuantity : float
            quantity of currency to obtain
        market_id : str
            market pair example(btc-clp)
        """
        exchangesPrices = self.get_prices(market_id)
        orderExchanges = self.order_prices(exchangesPrices);
        results = []
        for exchange in orderExchanges:
            quantity = currencyQuantity/exchange["price"][0]
            results.append({exchange["name"]: quantity})
        return results

    def __importClient(self, exchangeName):
        """
        Parameters
        ----------
        exchangeName : str
            name of exchange example(buda)
        """
        mod = __import__(f'src.infrastructure.clients.{exchangeName}', fromlist=[exchangeName.capitalize()])
        klass = getattr(mod, exchangeName.capitalize())
        return klass()
    
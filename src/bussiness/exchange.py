from src.infrastructure.clients.rates import Rates

class Exchange:
    """
    A class used to represent an Exchange

    ...

    Attributes
    ----------
    additionalParams : dict
        a list of additional params for a client
    name : str
        the name of the exchange
    client : ExchangeInterfaz
        infrastructure client class
    rates : Rates
        infrastructure client rates class

    Methods
    -------
    get_name()
        get exchange name
    get_ticker(market_id)
        get the ticker object from the exchange, 
        with rate and the usd conversion applied
    __findCurrency()
        utility function that find currency in the exchange 
        configuration list
    """
    def __init__(self, name, additionalParams, client):
        self.additionalParams = additionalParams
        self.name = name
        self.client = client
        self.rates = Rates();
        
    def get_name(self):
        return self.name
        
    def get_ticker(self, market_id):
        """
        Parameters
        ----------
        market_id : MarketId
            The market id object to found
        """
        currencyPivote = market_id.pair[1]
        usdcPrice = 1 
        if not self.__findCurrency(currencyPivote):
            usdcPrice = self.rates.get_usdc_price(f'usdc-{currencyPivote}')
       
        additionalRate = 1;
        if "additionalRate" in self.additionalParams:
            additionalRate += self.additionalParams["additionalRate"]

        return self.client.get_ticker(market_id, usdcPrice*additionalRate)
    
    def __findCurrency(self, currency):
        """
        Parameters
        ----------
        currency : str
            Currency to found
        """
        if len(list(filter(lambda currencyValid: currencyValid["name"] == currency.upper(), self.additionalParams["currencies"]))) > 0:
            return True
        else:
            return False
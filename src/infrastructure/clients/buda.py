import requests
from src.domain.ticker import Ticker
from src.domain.exceptions import ExchangeApiError
from src.domain.exchangeInterface import ExchangeInterface

class Buda(ExchangeInterface):
    """
    A class used to call buda api
    ...

    Methods
    -------
    get_ticker()
        call to buda api for ticker
    """
    def get_ticker(self, market_id, rate) -> Ticker:
        """Gets ticker from buda

        Parameters
        ----------
        market_id : MarketId
            The MarketId object 
        rate : long
           rate to applicate of ticker price

        Returns
        -------
        Ticker
            a ticker object
        """
        try:
            response = requests.get(f'https://www.buda.com/api/v2/markets/{market_id.pair[0]}-{market_id.pair[1]}/ticker')
            content = response.json()["ticker"]
        
            return Ticker([float(content["last_price"][0])*rate, content["last_price"][1]], 
                content["market_id"], 
                content["max_bid"], 
                content["min_ask"], 
                content["price_variation_24h"], 
                content["price_variation_7d"], 
                content["volume"])
        except requests.exceptions.HTTPError as e:
            raise ExchangeApiError(e)
        except requests.exceptions.Timeout:
            raise ExchangeApiError(e)
        except requests.exceptions.TooManyRedirects:
            raise ExchangeApiError(e)
        except requests.exceptions.RequestException as e:
            raise ExchangeApiError(e)
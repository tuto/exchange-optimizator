import requests
from src.domain.ticker import Ticker
from src.domain.exceptions import ExchangeApiError
from src.domain.exchangeInterface import ExchangeInterface

class Bitstamp(ExchangeInterface):
    """
    A class used to call bitstamp api
    ...

    Methods
    -------
    get_ticker()
        call to bitstamp api for ticker
    """
    def get_ticker(self, market_id, rate) -> Ticker:
        """Gets ticker from bitstamp

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
            response = requests.get(f'https://www.bitstamp.net/api/v2/ticker/{market_id.pair[0]}usd')
            jsonResponse = response.json()    
      
            return Ticker([float(jsonResponse["last"])*rate, f'{market_id.pair[1]}'.upper()], 
            f'{market_id.pair[0]}-{market_id.pair[1]}'.upper(), 
            jsonResponse["bid"], 
            jsonResponse["ask"], 
            jsonResponse["high"], 
            "", 
            jsonResponse["volume"])
        except requests.exceptions.HTTPError as e:
            raise ExchangeApiError(e)
        except requests.exceptions.Timeout:
            raise ExchangeApiError(e)
        except requests.exceptions.TooManyRedirects:
            raise ExchangeApiError(e)
        except requests.exceptions.RequestException as e:
            raise ExchangeApiError(e)
import requests
from src.domain.exceptions import ExchangeApiError

class Rates:
    """
    A class used to obtain the rate between 2 currencies
    ...

    Methods
    -------
    get_rate_price()
        call to buda api for obtain the rate between 2 currencies
    """
    def get_rate_price(self, pair) -> float:
        """Gets ticker from buda

        Parameters
        ----------
        pair : str
            a currency pair(BTC-CLP)

        Returns
        -------
        float
            a rate price
        """
        try:

            response = requests.get(f'https://www.buda.com/api/v2/markets/{pair}/ticker')
            jsonResponse = response.json()["ticker"]
            
            return float(jsonResponse["last_price"][0])
        except requests.exceptions.HTTPError as e:
            raise ExchangeApiError(e)
        except requests.exceptions.Timeout:
            raise ExchangeApiError(e)
        except requests.exceptions.TooManyRedirects:
            raise ExchangeApiError(e)
        except requests.exceptions.RequestException as e:
            raise ExchangeApiError(e)
import requests
from src.domain.ticker import Ticker
from src.domain.exchangeInterface import ExchangeInterface

class Bitstamp(ExchangeInterface):
    def get_ticker(self, market_id, rate):
        response = requests.get(f'https://www.bitstamp.net/api/v2/ticker/{market_id.pair[0]}usd')
        jsonResponse = response.json()    

        return Ticker([float(jsonResponse["last"])*rate, f'{market_id.pair[1]}'.upper()], 
        f'{market_id.pair[0]}-{market_id.pair[1]}'.upper(), 
        jsonResponse["bid"], 
        jsonResponse["ask"], 
        jsonResponse["high"], 
        "", 
        jsonResponse["volume"])

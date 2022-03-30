import requests
from src.domain.ticker import Ticker
from src.domain.exchangeInterface import ExchangeInterface

class Buda(ExchangeInterface):
    def get_ticker(self, market_id, rate):
        response = requests.get(f'https://www.buda.com/api/v2/markets/{market_id.pair[0]}-{market_id.pair[1]}/ticker')
        content = response.json()["ticker"]
        return Ticker([float(content["last_price"][0])*rate, content["last_price"][1]], 
            content["market_id"], 
            content["max_bid"], 
            content["min_ask"], 
            content["price_variation_24h"], 
            content["price_variation_7d"], 
            content["volume"])

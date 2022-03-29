import requests
from src.domain.ticker import Ticker
from src.domain.marketid import MarketId

from src.domain.exchangeInterface import ExchangeInterface
from src.infrastructure.clients.bitstamp import get_ticker
from src.infrastructure.clients.buda import get_ticker as get_ticker_buda

class Bitstamp(ExchangeInterface):

    def __init__(self):
        self.additionalParams = {}

    def setAdditionalParams(self, params):
        self.additionalParams = params
        
    def get_name(self):
        return "bistamp";

    def get_ticker(self, market_id):
    
        content = get_ticker(market_id)
        usdc_price = self.__get_usdc_currency_price(market_id)
        additionalRate = 1;
        if "additionalRate" in self.additionalParams:
            additionalRate += self.additionalParams["additionalRate"]

        return Ticker([float(content["last"])*usdc_price*additionalRate, f'{market_id.pair[1]}'.upper()], 
        f'{market_id.pair[0]}-{market_id.pair[1]}', 
        content["bid"], 
        content["ask"], 
        content["high"], 
        "", 
        content["volume"])
    
    def __get_usdc_currency_price(self, market_id):
        ticker = get_ticker_buda( MarketId(f'usdc-{market_id.pair[1]}'))
        return float(ticker["last_price"][0])

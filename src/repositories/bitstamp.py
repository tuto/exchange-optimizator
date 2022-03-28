import requests
from src.domain.ticker import Ticker
from src.infrastructure.clients.bitstamp import get_ticker
from src.infrastructure.clients.mindicador import get_rate
class Bitstamp:

    def __init__(self):
        self.additionalParams = {}

    def setAdditionalParams(self, params):
        self.additionalParams = params
        
    def get_name(self):
        return "bistamp";

    def get_ticker(self, market_id):
    
        content = get_ticker(market_id)
        rate = get_rate()
        additionalRate = 1;
        if "additionalRate" in self.additionalParams:
            additionalRate += self.additionalParams["additionalRate"]

        return Ticker([float(content["last"])*float(rate)*additionalRate, f'{market_id.pair[1]}'.upper()], 
        f'{market_id.pair[0]}-{market_id.pair[1]}', 
        content["bid"], 
        content["ask"], 
        content["high"], 
        "", 
        content["volume"])
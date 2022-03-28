import requests
from src.domain.ticker import Ticker
from src.infrastructure.clients.buda import get_ticker

class Buda:
    def __init__(self):
        self.additionalParams = {}

    def setAdditionalParams(self, params):
        self.additionalParams = params
        
    def get_name(self):
        return "buda"
        
    def get_ticker(self, market_id):
        content = get_ticker(market_id)
    
        return Ticker([float(content["last_price"][0]), content["last_price"][1]], 
        content["market_id"], 
        content["max_bid"], 
        content["min_ask"], 
        content["price_variation_24h"], 
        content["price_variation_7d"], 
        content["volume"])

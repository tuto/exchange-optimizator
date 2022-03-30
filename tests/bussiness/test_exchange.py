from src.infrastructure.clients.buda import Buda
from src.domain.ticker import Ticker
from src.domain.marketid import MarketId
import unittest
from unittest.mock import patch, MagicMock

class TestMarketId(unittest.TestCase):


    @patch('src.infrastructure.clients.rates.Rates')
    def test_get_ticker(self, rates):
        from src.bussiness.exchange import Exchange
        additionalParams={'additionalRate': 0.01, 'currencies': [{'name': 'CLP'}, {'name': 'COP'}, {'name': 'BTC'}, {'name': 'ETH'}]}
        ticker = Ticker([10.1, "CLP"], 
            "btc-clp", 
            "10", 
            "10", 
            "10", 
            "10", 
            "10")
        rates.get_usdc_price.return_value = 1 
        buda = Buda()
        buda.get_ticker = MagicMock(return_value = ticker)
        exchange = Exchange("buda", additionalParams, buda)
        tickerResponse = exchange.get_ticker(MarketId("btc-clp"));
        self.assertEqual(exchange.get_name(), "buda")
        self.assertEqual(exchange.additionalParams, additionalParams)
        self.assertEqual(ticker, tickerResponse)

        additionalParams={'additionalRate': 0.01, 'currencies': [{'name': 'USD'}]}
        exchange = Exchange("buda", additionalParams, buda)
        tickerResponse = exchange.get_ticker(MarketId("btc-clp"));
        self.assertEqual(ticker, tickerResponse)
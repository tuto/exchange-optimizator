from src.infrastructure.clients.rates import Rates
from src.domain.ticker import Ticker
from src.domain.marketid import MarketId
import unittest
from unittest.mock import patch, MagicMock
import  json

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

mockResponse = MockResponse({
            "ticker": {
                "last_price": ["879789.0", "CLP"],
                "market_id": "BTC-CLP",
                "max_bid": ["879658.0", "CLP"],
                "min_ask": ["876531.11", "CLP"],
                "price_variation_24h": "0.005",
                "price_variation_7d": "0.1",
                "volume": ["102.0", "BTC"]
            }}, 200)


def mocked_requests_get(*args, **kwargs):
    if args[0].find('https://www.buda.com/api/v2/markets/') != -1:
        return mockResponse

class TestMarketId(unittest.TestCase):
    @patch('src.infrastructure.clients.rates.requests.get', side_effect=mocked_requests_get)
    def test_get_ticker(self, mocked_requests_get):
        rates = Rates();
        tickerResponse = rates.get_usdc_price(MarketId("btc-clp"))
        self.assertEqual(879789.0, tickerResponse)
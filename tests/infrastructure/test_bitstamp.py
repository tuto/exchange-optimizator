from src.infrastructure.clients.bitstamp import Bitstamp
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
    "high": "47759.56",
    "last": "47047.24",
    "timestamp": "1648670134",
    "bid": "47009.08",
    "vwap": "47268.10",
    "volume": "1767.36593153",
    "low": "46572.15",
    "ask": "47028.74",
    "open": "47459.03"
    }, 200)

tickerResponseExpected = Ticker([470.4724, 'CLP'], 'BTC-CLP', '47009.08',  '47028.74', '47759.56',  '', '1767.36593153')

def mocked_requests_get(*args, **kwargs):
    if args[0].find('https://www.bitstamp.net/api/v2/ticker/') != -1:
        return mockResponse

class TestMarketId(unittest.TestCase):
    @patch('src.infrastructure.clients.bitstamp.requests.get', side_effect=mocked_requests_get)
    def test_get_ticker(self, mocked_requests_get):
        bitstamp = Bitstamp();
        tickerResponse = bitstamp.get_ticker(MarketId("btc-clp"), 0.01)
        self.assertEqual(tickerResponseExpected.last_price, tickerResponse.last_price)
        self.assertEqual(tickerResponseExpected.market_id, tickerResponse.market_id)
        self.assertEqual(tickerResponseExpected.max_bid, tickerResponse.max_bid)
        self.assertEqual(tickerResponseExpected.min_ask, tickerResponse.min_ask)
        self.assertEqual(tickerResponseExpected.price_variation_24h, tickerResponse.price_variation_24h)
        self.assertEqual(tickerResponseExpected.price_variation_7d, tickerResponse.price_variation_7d)
        self.assertEqual(tickerResponseExpected.volume, tickerResponse.volume)

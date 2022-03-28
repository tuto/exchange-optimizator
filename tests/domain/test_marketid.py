from src.domain.marketid import MarketId
from src.domain.exceptions import MarketIdFormatError
import unittest

class TestMarketId(unittest.TestCase):
    def test_normal_market_id(self):
        self.assertTrue(MarketId("btc-clp").pair[0], "btc")
        self.assertTrue(MarketId("btc-clp").pair[1], "clp")

    def test_exception_for_format_wrong(self): 
        with self.assertRaises(MarketIdFormatError):
            MarketId("btcclp")
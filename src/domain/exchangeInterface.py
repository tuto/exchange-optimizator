class ExchangeInterface:
    def setAdditionalParams(self, params):
        """Set additional params to exchange"""
        pass

    def get_name(self):
        """Return name of exchange"""
        pass
    
    def get_ticker(self, market_id):
        """Return the ticker"""
        pass
class Ticker:
    """
    A class used to represent a ticker object.
    The domain of this object is the buda ticker domain (https://api.buda.com/#ticker)
    ...

    Attributes
    ----------
    lastPrice : str
        last price of the last order
    marketId : str
        market id
    maxBid : str
        max bid order price
    minAsk : str
        min ask order price
    priceVariation24Hours : str
        how the price change the last 24 hours
    priceVariation7d : str
        how the price change the last 24 hours
    volume : str
        transactions volume the las 24 hours
    """
    def __init__(self, lastPrice, marketId, maxBid, minAsk, priceVariation24Hours, priceVariation7d, volume):

        self.last_price = lastPrice
        self.market_id = marketId
        self.max_bid = maxBid
        self.min_ask = minAsk
        self.price_variation_24h = priceVariation24Hours
        self.price_variation_7d = priceVariation7d
        self.volume = volume
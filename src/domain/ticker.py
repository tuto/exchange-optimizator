class Ticker:
    def __init__(self, lastPrice, marketId, maxBid, minAsk, priceVariation24Hours, priceVariation7d, volume):

        self.last_price = lastPrice
        self.market_id = marketId
        self.max_bid = maxBid
        self.min_ask = minAsk
        self.price_variation_24h = priceVariation24Hours
        self.price_variation_7d = priceVariation7d
        self.volume = volume
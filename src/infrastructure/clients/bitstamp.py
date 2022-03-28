import requests

def get_ticker(market_id):
    response = requests.get(f'https://www.bitstamp.net/api/v2/ticker/{market_id.pair[0]}usd')
    return response.json()    

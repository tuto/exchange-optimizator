import requests

def get_ticker(market_id):
    response = requests.get(f'https://www.buda.com/api/v2/markets/{market_id.pair[0]}-{market_id.pair[1]}/ticker')
    return response.json()["ticker"]

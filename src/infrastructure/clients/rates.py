import requests

class Rates:
    def get_usdc_price(self, pair):
        response = requests.get(f'https://www.buda.com/api/v2/markets/{pair}/ticker')
        jsonResponse = response.json()["ticker"]
        
        return float(jsonResponse["last_price"][0])
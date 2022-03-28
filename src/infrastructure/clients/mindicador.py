import requests

def get_rate():
    response = requests.get(f'https://mindicador.cl/api/dolar')
    return response.json()["serie"][0]["valor"]
  
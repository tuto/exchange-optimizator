
import sys, argparse
from loaderConfig import get_exchange_config
from src.bussiness.exchangelist import ExchangeList

def calculateAmmount(market_id, currencyQuantity, additionalRate): 
    exchangelist = ExchangeList()
    config = get_exchange_config()
    for exchange in config["exchanges"]:
        exchangelist.add(exchange["name"], {"additionalRate": additionalRate})

    exchanges = exchangelist.get_prices(market_id)
    orderExchanges = exchangelist.order_prices(exchanges);
    return exchangelist.calculateCurrencyRate(currencyQuantity, orderExchanges)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', help='market-id (ex: btc-clp)')
    parser.add_argument('-q', help='currency quantity (ex: 1000000)')
    parser.add_argument('-r', help='additional rate to usdc change from local currency(ex: 0.01)')
    args = vars(parser.parse_args())   
    print(calculateAmmount(args["m"], float(args["q"]), float(args["r"])))

if __name__ == "__main__":
   main()
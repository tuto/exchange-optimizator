
import sys, argparse
from loaderConfig import get_exchange_config
from src.bussiness.exchangelist import ExchangeList
from src.domain.exceptions import MarketIdFormatError

def calculateAmmount(market_id, currencyQuantity, additionalRate): 
    exchangelist = ExchangeList()
    config = get_exchange_config()
    for exchange in config["exchanges"]:
        exchangelist.add(exchange["name"], {"additionalRate": additionalRate, "currencies": exchange["currencies"]})

    return exchangelist.calculateCurrencyRate(currencyQuantity, market_id)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', help='market-id (ex: btc-clp)', default=None, required=True)
    parser.add_argument('-q', help='currency quantity (ex: 1000000)', default=None, required=True)
    parser.add_argument('-r', help='additional rate to usdc change from local currency(ex: 0.01)', default=None, required=True)
    args = vars(parser.parse_args())   
    try:
        if args["m"].upper() != "BTC-CLP" :
            print("for now, only btc-clp is supported")
            return
        print(calculateAmmount(args["m"], float(args["q"]), float(args["r"])))
    except MarketIdFormatError as e:
        print("The market id format is wrong")
        SystemExit()

if __name__ == "__main__":
   main()
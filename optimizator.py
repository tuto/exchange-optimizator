
from src.bussiness.exchangelist import ExchangeList

exchangelist = ExchangeList();
exchangelist.add("buda");
exchangelist.add("bitstamp", {"additionalRate": 0.01});

print(exchangelist.get_minimun_ticker("btc-clp"))
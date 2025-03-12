import pybithumb
import json
import datetime
# tickers = pybithumb.get_tickers()
# print(len(tickers))

# detail = pybithumb.get_market_detail("BTC")
# print(json.dumps(detail, indent=2, ensure_ascii=False))

# orderbook = pybithumb.get_orderbook("BTC")
# print(json.dumps(orderbook, indent=2, ensure_ascii=False))

# ms = int(orderbook["timestamp"])
# dt = datetime.datetime.fromtimestamp(ms / 1000)
# print(dt)

all = pybithumb.get_current_price("ALL")

for ticker, data in all.items():
    print(ticker, data["fluctate_rate_24H"])

btc = pybithumb.get_ohlcv("BTC")
close_series = btc["close"]
print(close_series)
#!/usr/bin/env python3
import ccxt.async as ccxt

# print(ccxt.exchanges)

binance = ccxt.binance ()
markets = binance.load_markets ()
print (binance.id, markets)
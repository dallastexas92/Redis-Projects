#!/usr/bin/env python

import redis
import sys
import json

client = redis.Redis(host='localhost', port=6379)
stream = "updates"

# Grab the JSON and update the price
j = client.hget("instrument:{}".format(sys.argv[1]), "json")
instrument = json.loads(j)

print(instrument)

if "MAINLIST" in instrument["watchlists"]:
	print("already in watchlist")
else:
	instrument["watchlists"].append("MAINLIST")
	client.hset(
	        "instrument:%s" %(instrument["instrument"]),
	        mapping = {
	            "ticker": instrument["instrument"],
	            "exchange": instrument["tickers"]["exchange"],
	            "price": instrument["price"],
	            "subindex": ",".join(instrument["tickers"]["subindex"]),
	            "watchlists": ",".join(instrument["watchlists"]),
	            "json": json.dumps(instrument)
	            })
	client.xadd(stream, {"type": "watchlist", "values": "updated"})

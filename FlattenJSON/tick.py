#!/usr/bin/env python

from redisearch import Client, Query
import sys
import json

stream = "updates"


load_client = Client(
        'IdxInstruments',
        host="localhost",
        port=6379,
        password="",
        )

# Grab the JSON and update the price
j = load_client.redis.hget("instrument:{}".format(sys.argv[1]), "json")
instrument = json.loads(j)

instrument["price"] = round(float(instrument["price"])*1.01, 2)
load_client.redis.hset(
        "instrument:%s" %(instrument["instrument"]),
        mapping = {
            "ticker": instrument["instrument"],
            "exchange": instrument["tickers"]["exchange"],
            "price": instrument["price"],
            "subindex": ",".join(instrument["tickers"]["subindex"]),
            "watchlists": ",".join(instrument["watchlists"]),
            "json": json.dumps(instrument)
            })


z = load_client.search(Query("@ticker:%s @watchlists:{MAINLIST}" %(sys.argv[1])))
if len(z.docs) == 1:
        load_client.redis.xadd(stream, {"type": "instrument", "values": z.docs[0].json})
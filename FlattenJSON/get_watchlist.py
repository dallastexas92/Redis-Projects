#!/usr/bin/env python

from redisearch import Client, Query

load_client = Client(
        'IdxInstruments',
        host="localhost",
        port=6379,
        password="",
        )

z = load_client.search(Query("@watchlists:{MAINLIST}"))
for d in z.docs:
	print(d.ticker)
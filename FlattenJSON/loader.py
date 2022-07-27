#!/usr/bin/env python

from redisearch import Client, IndexDefinition, TextField, NumericField, TagField, Query
import json

load_client = Client(
        'IdxInstruments-v1',
        host="localhost",
        port=6379,
        password="",
        )

definition = IndexDefinition(
        prefix=['instrument:'],
        )

load_client.create_index(
        (
            TextField("ticker", sortable=True),
            TextField("exchange"),
            NumericField('price'),
            TagField('subindex'),
            TagField('watchlists')
            ),
        definition=definition)

with open('./data.json', encoding='utf-8') as myfile:
    for line in myfile:
        instrument = json.loads(line)
        load_client.redis.hset(
                "instrument:%s" %(instrument["instrument"]),
                mapping = {
                    "ticker": instrument["instrument"],
                    "exchange": instrument["tickers"]["exchange"],
                    "price": instrument["price"],
                    "subindex": ",".join(instrument["tickers"]["subindex"]),
                    "watchlists": ",".join(instrument["watchlists"]),
                    "json": line
                    })


load_client.aliasadd("IdxInstruments")

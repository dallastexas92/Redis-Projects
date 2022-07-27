#!/usr/bin/env python

import redis

client = redis.Redis(host='localhost', port=6379)
stream = "updates"
group = "mygroup"
consumer = "{}-consumer".format(group)

try:
    client.xgroup_create(stream, group, mkstream=True)

except:
    print("Group {} already exists".format(group))

while True:
    msg = client.xreadgroup(group, consumer, {stream : ">"}, 2, block=5000)
    if msg:
        for m in msg[0][1]:
            if m[1][b'type'].decode('utf-8') == "instrument":
                print("Updated Instrument on Watchlist")
                print(m[1][b'values'].decode('utf-8'))
            elif m[1][b'type'].decode('utf-8') == "watchlist":
                print("Updated Watchlist - please re-pull")
            else:
                print("unknown message type")

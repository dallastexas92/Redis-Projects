import redis
import random
import time
import sys

host = "34.73.199.143" #"redis-17902.dallas-east.demo.redislabs.com"
port = 17902
password = ""
r = redis.StrictRedis(host = host, port = port, password = password, charset="utf-8", decode_responses=True)

loop = 0
i = 0
retry=0
connected = True

r.set("key", "-1")

while connected:
    try:
        while loop < 10000:
            keyName = "key:"+str(loop)
            r.set(keyName,loop)
            time.sleep(.005)
            print(r.get(keyName))
            loop+=1
        break
    except redis.ConnectionError:
        print("Oh no, a failure!")
        #print("Connection Error, retry %s" % retry)
        #time.sleep(1)
        #retry +=
        r = redis.StrictRedis(host = "35.243.240.14", port = port, password = password, charset="utf-8", decode_responses=True)
        #print("And we are live!")
#print("'# of Retries: %s" % retry)
sys.exit()

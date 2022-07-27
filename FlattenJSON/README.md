# Running examples

## Prerequisites

(Docker)[https://docker.io]

(Python3)[https://www.python.org/downloads/]


## Running

1) Setup virtual env

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2) Load the Data

```
./loader.py
```

3) Start the example listener that will listen for updates in a separate window

```
./example_listener.py
```

4) Modify a stock on the watchlist by ticking up the price

```
./tick.py GOOG

5) Modify a stock not on the  watchlist and notice no updates

```
./tick.py MSBHF
```

6) Add MSBHF to the watchlist

```
./add_to_watchlist.py MSBHF
```

7) Modify the stock again and you should see the update in the listener

```
./tick.py MSBHF
```

8) Dump the whole watchlist

```
./get_watchlist.py
```

import sys
import urllib.request
import json
from datetime import date,timedelta

start = date.today() - timedelta(int(sys.argv[1]))
today = date.today().isoformat()

# get data
rBtc = (urllib.request
.urlopen(f'https://api.gdax.com/products/BTC-USD/candles?start={start}&end={today}&granularity=86400')
.read().decode('utf-8'))

rEth = (urllib.request
.urlopen(f'https://api.gdax.com/products/ETH-USD/candles?start={start}&end={today}&granularity=86400')
.read().decode('utf-8'))

rLtc = (urllib.request
.urlopen(f'https://api.gdax.com/products/LTC-USD/candles?start={start}&end={today}&granularity=86400')
.read().decode('utf-8'))

# deserialize
btc = json.loads(rBtc)[::-1]
eth = json.loads(rEth)[::-1]
ltc = json.loads(rLtc)[::-1]

# write
f = open('/out/close_price.csv', 'w')
i = 0
for day in btc:
  line = date.fromtimestamp(day[0]).isoformat() + ',' + str(day[4])
  line += ',' + str(eth[i][4])
  line += ',' + str(ltc[i][4])
  f.write(line + '\n')
  i = i + 1
f.close()
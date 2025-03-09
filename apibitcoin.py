import pandas as pd

from pycoingecko import CoinGeckoAPI
cg=CoinGeckoAPI()
bitcoin_data=cg.get_coin_market_chart_by_id(id='bitcoin',vs_currency='usd',days=30)

prices= bitcoin_data['prices']
data =pd.DataFrame(prices,columns=['TimeStamp','Price'])
data['Date']=pd.to_datetime(data['TimeStamp'], unit ='ms')

print(data[['Date', 'Price']])

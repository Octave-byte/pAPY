# -*- coding: utf-8 -*-

# Import the os module
import os
import pandas as pd
import numpy as np
from datetime import date
import requests
from pandas import json_normalize 

###############
## Data prep
###############

r = requests.get('https://iunmfujgowtioifurpcp.supabase.co/rest/v1/historical_price?select=*', headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaWF0IjoxNjQzMzEyNjE1LCJleHAiOjE5NTg4ODg2MTV9.SZ9vqTxuLt9-kEPXvVzg5RTyzL-3VFn5QvIZirpBgO8', 'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaWF0IjoxNjQzMzEyNjE1LCJleHAiOjE5NTg4ODg2MTV9.SZ9vqTxuLt9-kEPXvVzg5RTyzL-3VFn5QvIZirpBgO8'})
r2 = requests.get('https://iunmfujgowtioifurpcp.supabase.co/rest/v1/historical_tvl?select=*', headers={'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaWF0IjoxNjQzMzEyNjE1LCJleHAiOjE5NTg4ODg2MTV9.SZ9vqTxuLt9-kEPXvVzg5RTyzL-3VFn5QvIZirpBgO8', 'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoic2VydmljZV9yb2xlIiwiaWF0IjoxNjQzMzEyNjE1LCJleHAiOjE5NTg4ODg2MTV9.SZ9vqTxuLt9-kEPXvVzg5RTyzL-3VFn5QvIZirpBgO8'})

priceYearn = r.json()
tvlYearn = r2.json()
price = json_normalize(priceYearn)
tvl = json_normalize(tvlYearn)

###################
#APY table
###################


combined = pd.merge( price, tvl,on=['protocol_id', 'blocktime', 'address', 'timestamp'])



combined['dailyAPY'] = (combined.groupby('address')['price']
                                  .apply(pd.Series.pct_change)*365)

combined['weeklyAPY'] = (combined.groupby('address')['price']
                                  .apply(lambda dfi : dfi.pct_change(periods=7))*365/7)

combined['monthlyAPY'] = (combined.groupby('address')['price']
                                  .apply(lambda dfi : dfi.pct_change(periods=30))*365/30)


combined['daily'] = (combined.groupby('address')['price']
                                  .apply(pd.Series.pct_change))

combined['count'] = combined.groupby("address").apply(lambda x: np.arange(1, len(x)+1))[0]


combined['inceptionAPY'] = ((1 + combined.daily).cumprod() - 1)*365/(combined['count'])

historical_apy = combined.drop(['id_x', 'id_y', 'price', 'blocktime', 'daily', 'count'], 1)



###################
#Statistics table
###################

final  = combined.drop_duplicates('address')[['address', 'protocol_id']]



corr_weekly = combined.dropna(subset=['weeklyAPY']).groupby('address')[['weeklyAPY', 'tvl']].corr().unstack().iloc[:,1].to_frame(name = "corr_w")
corr_monthly = combined.dropna(subset = ['monthlyAPY']).groupby('address')[['monthlyAPY','tvl']].corr().unstack().iloc[:,1].to_frame(name = "corr_m")
vol_weekly = combined.dropna(subset=['weeklyAPY']).groupby('address')[["weeklyAPY"]].std()
vol_monthly = combined.dropna(subset = ['monthlyAPY']).groupby('address')[["monthlyAPY"]].std()



final = pd.merge(corr_weekly, final, on = ['address'])
final = pd.merge(corr_monthly, final, on = ['address'])
final = pd.merge(vol_weekly, final, on = ['address'])
final = pd.merge(vol_monthly, final, on = ['address'])
final[['timestamp']] = date.today()
final[['id']] = 0

historical_stats = final.rename(columns={"monthlyAPY": "vol_m", "weeklyAPY": "vol_w"})





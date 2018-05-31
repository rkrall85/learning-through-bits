import pandas as pd
import quandl, math
import numpy as np


quandl.ApiConfig.api_key = 'Tzgx-76RsxHryzAy6py1'
df = quandl.get('WIKI/GOOGL')#google stock prices

#print(df.head())
#list of features we want (i.e. columns)
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
#create high minus low percentage change (high - low / low)
df['HL_PCT'] = (df['Adj. High']- df['Adj. Close'])/df['Adj. Close']*100.0
#daily percentage change
df['PCT_Change'] = (df['Adj. Close']- df['Adj. Open'])/df['Adj. Open']*100.0
#create new data frame
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]
#variable for forcast column
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True) #will be an outliner later; updating None values to -99999

#cast as int (math.ceil returns float), round to nearest whole number, go out 10 days
forecast_out = int(math.ceil(0.01*len(df))) #number of days out (trying to predict 10 days out)
print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out) #grabbing the adj. close value 35 days ahead
df.dropna(inplace=True)
print(df.head(35))

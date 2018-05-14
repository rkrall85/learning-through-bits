import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')

#print(df.head())


df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
#create percent column
df['HL_PCT'] = (df['Adj. High']- df['Adj. Close'])/df['Adj. Close']*100.0
#percent change
df['PCT_Change'] = (df['Adj. Close']- df['Adj. Open'])/df['Adj. Open']*100.0
#clean new data frame
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]
#print(df.head())

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True) #will be an outliner later; updating None values to -99999

forecast_out = int(math.ceil(0.01*len(df))) #number of days out (trying to predict 10 days out)

df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)

print(df.head())

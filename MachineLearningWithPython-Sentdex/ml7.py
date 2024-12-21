import pandas as pd
import quandl, math, datetime
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle




style.use('ggplot')


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
forecast_out = int(math.ceil(0.01*len(df))) #number of days out (trying to predict 35 days out)

df['label'] = df[forecast_col].shift(-forecast_out) #grabbing the adj. close value 35 days ahead


X = np.array(df.drop(['label'],1)) #returning a new data frame withou label column and saving it in X
x = preprocessing.scale(X)
X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
####different regression models####
        #linear regression
#clf = LinearRegression()
#clf = LinearRegression(n_jobs=-1) #multi threading
        #svm regression
#clf = svm.SVR()
#clf = svm.SVR(kernel='poly')
###################################

#clf.fit(X_train, y_train)
#save the training classifier
#with open('linearregression.pickle','wb') as f:
#    pickle.dump(clf, f)

pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test) #aka confidence

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)
df['Forecast'] = np.nan

#dates for graph
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day


for i in forecast_set:
    next_date = datetime.datetime. fromtimestamp(next_unix)
    next_unix += one_day
    #list of values and the forecast
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

#Creating the graph
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

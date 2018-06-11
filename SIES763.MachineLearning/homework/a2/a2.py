#Robert Krall
#SEIS763
#Assignment 2


import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
import pandas as pd

#import csv
input_file  = open('patients.csv','r')  #read mode
df = pd.read_csv(input_file, sep=",")
#df.columns = ["Age","Diastolic","Gender","Height","LastName","Location","SelfAssessedHealthStatus","Smoker","Systolic","Weight"]#leave out if there is a header

#get dummies for categorical columns
dummies = pd.get_dummies(df[['Gender','Location','SelfAssessedHealthStatus']], drop_first=True)
cleaned_df = pd.concat([df,dummies], axis=1)
cleaned_df.drop(['Gender','Location','SelfAssessedHealthStatus'], axis=1, inplace=True)

#X and y values
X = cleaned_df[['Age',"Gender_'Male'",'Height','Weight','Smoker'
                    ,"Location_'St. Mary's Medical Center'"
                    ,"Location_'VA Hospital'"
                    ,"SelfAssessedHealthStatus_'Fair'"
                    ,"SelfAssessedHealthStatus_'Good'"
                    ,"SelfAssessedHealthStatus_'Poor'"]]
y = cleaned_df[["Systolic"]]


# Question 4 - The coefficients
#create linear regression object
regr = linear_model.LinearRegression()
#training the model
regr.fit(X, y)
print('Coefficients: \n', regr.coef_ )

y_pred = regr.predict(X)

print(mean_squared_error(y, y_pred))
print(r2_score(y, y_pred))


#plot out the outputs

#plt.scatter(X, y, color='black')

print(X.shape)
print(y.shape)

#Robert Krall
#SEIS763
#Assignment 2


import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import DistanceMetric
import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd

#import csv
input_file  = open('patients.csv', 'r')  #read mode
df = pd.read_csv(input_file, sep=",")

#get dummies for categorical columns
dummies = pd.get_dummies(df[['Gender','Location','SelfAssessedHealthStatus']], drop_first=True)
#adding dummy columns to our dataframe
cleaned_df = pd.concat([df,dummies], axis=1)
#dropping columns in dataframe that are used for dummy columns since they are not wanted anymore
cleaned_df.drop(['Gender','Location','SelfAssessedHealthStatus'], axis=1, inplace=True)

#X and y values
X = cleaned_df[['Age',"Gender_'Male'",'Height','Weight','Smoker'
                    ,"Location_'St. Mary's Medical Center'"
                    ,"Location_'VA Hospital'"
                    ,"SelfAssessedHealthStatus_'Fair'"
                    ,"SelfAssessedHealthStatus_'Good'"
                    ,"SelfAssessedHealthStatus_'Poor'"]]
y = cleaned_df[["Systolic"]]

#rename columns so its easier to use later on
cleaned_df = cleaned_df.rename(columns={"Gender_'Male'": "Gender_Male",
        "Location_'St. Mary's Medical Center'": "Location_StMarysMedicalCenter",
        "Location_'VA Hospital'" : "Location_VAHospital",
        "SelfAssessedHealthStatus_'Fair'": "SelfAssessedHealthStatus_Fair",
        "SelfAssessedHealthStatus_'Good'": "SelfAssessedHealthStatus_Good",
        "SelfAssessedHealthStatus_'Poor'": "SelfAssessedHealthStatus_Poor"
        })



#print(cleaned_df.head())


# Question 4 - The coefficients
#create linear regression object
regr = linear_model.LinearRegression()
#training the model
regr.fit(X, y)
y_pred = regr.predict(X)

#the coefficients
print("MSE: %2f" %mean_squared_error(y, y_pred))
print("Variance Score: %2f" %r2_score(y, y_pred))

#plot outputs
plt.scatter(X, y, color='black')
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.xticks(());
plt.yticks(());
plt.show();


#print('Coefficients: \n', regr.coef_ )

#fit linear_model
#model = sm.OLS(y,X)
#results = model.fit()

#outliers
#outliers = sm.regression.linear_model.OLSResults.outlier_test(results)
#print(sm.regression.linear_model.OLSInfluence.summary_frame(results))

#dist = DistanceMetric.get_metric('euclidean')

#concating all the column names together
model_columns ="Systolic ~ Age + Gender_Male +  Height + Weight + "
model_columns += "Location_StMarysMedicalCenter + Location_VAHospital + "
model_columns += "SelfAssessedHealthStatus_Fair + SelfAssessedHealthStatus_Good + SelfAssessedHealthStatus_Poor"

#model1 = ols('Systolic ~ Age + Gender_Male +  Height + Weight + Smoker + Location_StMarysMedicalCenter + Location_VAHospital + SelfAssessedHealthStatus_Fair + SelfAssessedHealthStatus_Good + SelfAssessedHealthStatus_Poor', data=cleaned_df).fit()
#model1 = ols(model_columns, data=cleaned_df).fit()
#print(model1.summary())
#print(model1.cooks_distance())
#fig, ax = plt.subplots(figsize=(12,8))
#fig = sm.graphics.influence_plot(model1, ax=ax, criterion="cooks")

#fig





#print(regr.score(X,y))

#y_pred = regr.predict(X)

#print(mean_squared_error(y, y_pred))
#print(r2_score(y, y_pred))


#plot out the outputs

#plt.scatter(X, y, color='black')

#print(X.shape)
#print(y.shape)

#plt.plot(X,y)
#plt.show()
#print(OLSInfluence.summary_frame())

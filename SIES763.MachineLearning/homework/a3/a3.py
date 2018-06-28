
#Robert Krall
#SEIS 763
#assignment 2

import pandas as pd;
from scipy import stats; #used for Z Score
from sklearn import linear_model #for lasso model
import matplotlib.pyplot as plt #used to map the lasso plot
import numpy as np
from matplotlib.pyplot import axvline

#Step 1 import data

input_file  = open('patients.csv','r')  #read mode
patients_df = pd.read_csv(input_file, sep=",")#, header=None)

#Step 1. Set up dummy Variables
dummy_gender    = pd.get_dummies(patients_df['Gender']);
dummy_location  = pd.get_dummies(patients_df['Location']);
dummy_health    = pd.get_dummies(patients_df['SelfAssessedHealthStatus']);

X = pd.concat([patients_df, dummy_gender,dummy_location,dummy_health], axis=1)
X.drop(['Gender'], inplace=True, axis=1)
X.drop(['Location'], inplace=True, axis=1)
X.drop(['SelfAssessedHealthStatus'], inplace=True, axis=1)
X.drop(['LastName'], inplace=True, axis=1)

#Step 2. Normalize Data
z_cols = patients_df[['Age','Height','Weight']]
new_z = stats.zscore(z_cols)
df_values   = new_z
df_index    = [i for i in range(0, len(new_z))]
new_z2       = pd.DataFrame(df_values, df_index)
new_z2.columns = ['Age','Height','Weight']

X['Age'] = new_z2['Age'];
X['Height'] = new_z2['Height'];
X['Weight'] = new_z2['Weight'];X

y = patients_df['Systolic']
X.drop(['Systolic'], inplace=True, axis=1)

#Step 3 Lasso model
lm = linear_model.LassoLarsCV(cv=10).fit(X,y);
#B = reg.coef_;
#FitInfo =


m_log_alphas = -np.log10(lm.alphas_) #do this to make alphas (lambda) easier to read
ax = plt.gca()
plt.plot(m_log_alphas, lm.coef_path_.T)
#plt.axvline(-np.log10(lm.alpha_), linestlye='--', color='k',label='alpha CV')
plt.ylabel('Regression coefficients');
plt.xlabel('-log(alpha)');
plt.title('Regrssion Coefficients Progression For Lasso Paths');

plt.show()

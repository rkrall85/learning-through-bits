

#Robert Krall
#SEIS 763
#assignment 4

import pandas as pd;
from scipy import stats; #used for Z Score
from sklearn import linear_model #for lasso model
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn import metrics, cross_validation
import matplotlib.pyplot as plt #used to map the lasso plot
import numpy as np
from matplotlib.pyplot import axvline

#Step 1 import data

input_file  = open('CellDNA.csv', 'r')  #read mode
dna_df = pd.read_csv(input_file, sep=",", header=None)
dna_df.columns = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13"]#leave out if there is a header

#Step 2 Update last column to be a 1 or 0
#dna_df.loc[dna_df['13'] >= 1, '13'] = 1

#Step 3. Split up x and y values
X = dna_df.loc[:, dna_df.columns != '13']
y = dna_df['13']


#Step 3 Standardize the data
ZX = stats.zscore(X)
#convert numpy array to pandas df
df_index    = [i for i in range(0, len(ZX))]
ZX_df       = pd.DataFrame(ZX, df_index)

#Step 4. Create Lasso Model in python
#lm = linear_model.LassoCV(eps=0.0001, n_alphas=100,cv=10).fit(X2_df, y);
#lm = linear_model.LassoLarsCV(cv=10).fit(X2_df, y);
#print(X2_df)#starts at 1 and 13 columns
#print(y)

lrm = linear_model.LogisticRegressionCV(Cs=90,cv=10).fit(ZX, y);
#print("Interecpt, coefs")
#print(lrm.intercept_, lrm.coef_)





#lm = cross_validation.cross_val_predict(LogisticRegression(), X2_df, y, cv=10)




#rint("Accuracy of dataset: ",lrm.score(ZX,y))
#print("Look at coefficients:");
#print(lrm.coef_)
#print(lrm.classes_)
#print(pd.DataFrame(zip(X2_df.columns, np.transpose(logistic_model.coef_))))
#column_names = ['intercept'] + list(dna_df.columns)
#column_names = list(dna_df.columns)
#print(pd.DataFrame(column_names,np.transpose(logistic_model.coef_)))

#plt.plot(lrm.intercept_, lrm.coef_)


#print(logistic_model.intercept_)
#print('*'*100)
#print(logistic_model.cross_val_predict)


#print(logistic_model.intercept_, logistic_model.coef_)

#Step 5. Plot the results
#plot coefficient progression

#plt.plot(logistic_model.intercept_, logistic_model.coef_)


'''
m_log_alphas = -np.log10(lm.alphas_) #do this to make alphas (lambda) easier to read
ax = plt.gca()
plt.plot(m_log_alphas, lm.coef_path_.T)
#plt.axvline(-np.log10(lm.alpha_), linestlye='--', color='k',label='alpha CV')
plt.ylabel('Regression coefficients');
plt.xlabel('-log(alpha)');
plt.title('Regrssion Coefficients Progression For Lasso Paths');


plt.show()
'''

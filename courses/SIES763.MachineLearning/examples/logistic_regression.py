import numpy as np
from sklearn import linear_model, datasets

# import data, and use some
iris = datasets.load_iris()
#X = iris.data[:, :2] # use all records from first two features.
X = iris.data[50:, :2] # use records 51 to end from first two features.
#X = iris.data # use all 4 features.

Y = iris.target;
Y = Y[50:] # use only records 51 to end, so only 2 classes
# Inverse of regularization strength; smaller C ==> stronger regularization.
# LOSS = C * E + theta, default C = 1
logreg = linear_model.LogisticRegression()
# fit the data.
logreg.fit(X, Y)
logreg.predict(X) # predicted classes

print(logreg.intercept_, logreg.coef_, '\n')
print(logreg.predict(X), '\n')
print(logreg.predict_proba(X) , '\n')
print(logreg.predict_log_proba(X))

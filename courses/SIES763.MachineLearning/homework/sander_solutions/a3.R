# Install and import necessary packages
install.packages("glmnet")
install.packages("glmnetUtils")
install.packages("plotmo")
library(glmnet)
library(glmnetUtils)
library(plotmo)

# Read in the csv file
patients <- read.csv("~/Desktop/SEIS 763/patients.csv")

# Delete the columns that weren't included in the assignment
X = patients[,-2]
X = X[,-4]

# Standardize the numerical variables
X$Age =scale(X$Age)
X$Weight =scale(X$Weight)
X$Height =scale(X$Height)

# Create lasso regression model
lasso = glmnet(Systolic~., X)

# Plot lasso regression model
plot_glmnet(lasso, label=TRUE)

# Create 10-fold cross-validation model
cv = cv.glmnet(Systolic~., X, nfolds = 10)

# Plot 10-fold cross-validation model
plot(cv)

# Print coefficients for lambda value selecting top two predictors
coef(cv, s = 0.75)






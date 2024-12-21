# Install and import necessary packages
install.packages("glmnetUtils")
install.packages("plotmo")
library(glmnetUtils)
library(plotmo)

# Read in the csv file
dna <- read.csv("~/Desktop/SEIS 763/CellDNA.csv", header=FALSE)

# Change all non-zero variables for y variable to 1
dna$V14[dna$V14 > 0] <- 1

# Convert y variable to factor
dna$V14 = as.factor(dna$V14)

# Standardize the numerical variables
dna$V1 = scale(dna$V1)
dna$V2 = scale(dna$V2)
dna$V3 = scale(dna$V3)
dna$V4 = scale(dna$V4)
dna$V5 = scale(dna$V5)
dna$V6 = scale(dna$V6)
dna$V7 = scale(dna$V7)
dna$V8 = scale(dna$V8)
dna$V9 = scale(dna$V9)
dna$V10 = scale(dna$V10)
dna$V11 = scale(dna$V11)
dna$V12 = scale(dna$V12)
dna$V13 = scale(dna$V13)

# Create lasso regression model
lasso = glmnet(V14~., dna, alpha = 1, family = 'binomial')

# Plot lasso regression model
plot_glmnet(lasso, label=TRUE)
lasso

# Create 10-fold cross-validation model
cv = cv.glmnet(V14~., dna, alpha = 1, nfolds = 10, family = 'binomial', type.measure = 'mse')

# Plot 10-fold cross-validation model
plot(cv)

# Find lambda that minimizes the MSE
cv$lambda.1se

# Find coefficients of the predictors at the lambda that minimizes the MSE
coef(cv, s = 'lambda.1se')


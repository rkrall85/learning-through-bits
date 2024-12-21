library(MASS) #data sets to use
#install.packages('ISLR')
library(ISLR) #datasets in the book
## Simple Linear Regression
names(Boston)
?Boston #about Boston dataset
plot(medv-lstat,Boston)



#Nonlinear SVM

#load package
library(e1071)

#load data from website
load(url("http://www-stat.stanford.edu/~tibs/ElemStatLearn/datasets/ESL.mixture.rda"))

names(ESL.mixture) #output column names
rm(x,y,dat) #remove old xs and ys
attach(ESL.mixture)
plot(x,col=y+1) #plot the data as is

dat=data.frame(y=factor(y),x)#create dataframe

#Create model
fit = svm(factor(y)~.,data=dat,scale=FALSE, kernel="radial", cost=5)

#Create grid from the model
xgrid=expand.grid(X1=px1, X2= px2)
ygrid=predict(fit, xgrid)
plot(xgrid, col=as.numeric(ygrid),pch=20, cex=.2)
points(x, col=y+1, pch=19)

#create a curve to align with dots.
func=predict(fit, xgrid, decision.values = TRUE)
func=attributes(func)$decision

#create contour
contour(px1, px2, matrix(func,69,99), level=0, add=TRUE)
contour(px1, px2, matrix(func,69,99), level=.5, add=TRUE, col="blue",lwd=2)

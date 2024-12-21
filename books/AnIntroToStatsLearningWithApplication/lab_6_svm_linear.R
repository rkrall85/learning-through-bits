

#make some data
set.seed(10111)
x=matrix(rnorm(40),20,2)
y=rep(c(-1,1),c(10,10))


x
y

x[y==1,]=x[y==1,]+1
#pch=19 is the size of the dot
plot(x, col=y+3, pch=19)

#svm package is 'e1071'
library(e1071)
#create a data frame and convert y to factor rathe than digit
dat=data.frame(x,y=as.factor(y))

#linear svm classifier
svmfit=svm(y~., data=dat, kernel="linear", cost=10, scale=FALSE)
print(svmfit)#output stats of svm model
plot(svmfit,dat) #plot out svm model

#make function 75x75 grid
make.grid=function(x, n=75){
  grange=apply(x,2,range)
  x1=seq(from=grange[1,1],to=grange[2,1], length=n)
  x2=seq(from=grange[1,2],to=grange[2,2], length=n)
  expand.grid(X1=x1, X2=x2)
}
#create our own grid of the svm model
xgrid=make.grid(x)
ygrid=predict(svmfit, xgrid)
plot(xgrid,col=c("red","blue")[as.numeric(ygrid)],pch=20, cex=.2)
points(x,col=y+3, pch=19)
points(x[svmfit$index,],pch=5, cex=2)

#find the coefficents
beta=drop(t(svmfit$coefs)%*%x[svmfit$index,])
beta0=svmfit$rho
plot(xgrid,col=c("red","blue")[as.numeric(ygrid)],pch=20, cex=.2)
points(x,col=y+3, pch=19)
points(x[svmfit$index,],pch=5, cex=2)
abline(beta0/beta[2], -beta[1]/beta[2]) #svm line
abline((beta0-1)/beta[2], -beta[1]/beta[2], lty=2) #upper margin
abline((beta0+1)/beta[2], -beta[1]/beta[2], lty=2) #lower margin




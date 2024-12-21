## Vectors, data, matrices, and subsetting

x = c(2,7,5)
x
y = seq(from=4, length=3, by =3) #assing y with values
y #print y
?seq #output help doc
x+y
x/y
x^y
x[2]
x[2:3] #start at 2 and end at 3
x[-2] #remove element 2 and return new subset
x[-c(1,2)]
z=matrix(seq(1,12),4,3)
z
z[3:4, 2:3]
z[,2:3]
z[,1]
z[,1,drop=FALSE]
dim(z) #print dimension of z
ls() #variables in working directory
rm(y) #remote y
ls()
## Generating random data, graphics
x=runif(50)
y=rnorm(50)
plot(x,y)
plot(x,y,xlab="Random Uniform",ylab="Random Normal",pch="*", col="blue")
par(mfrow=c(2,1))
plot(x,y)
hist(y)
par(mfrow=x(1,1))

##Reading in data
Auto=read.csv("C:/Users/rkrall/github/AnIntroToStatsLearningWithApplication/chapter_2_stats_learning/Auto.csv")
names(Auto) #read header
dim(Auto) #output dim of file
class(Auto) #what type of object
summary(Auto) #stats summary of file
plot(Auto$cylinders, Auto$mpg)
attach(Auto) #create a workspace with all variables so you dont have to use $ sign
search()
plot(cylinders, mpg)
cylinders=as.factor(cylinders)

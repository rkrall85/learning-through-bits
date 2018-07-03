"
Robert Krall
SEIS 763
Assignment 5
"

#-----------Packages Need -------------#
#install.packages("e1071")
library(e1071)

#-----------Read File In----------------#
file_name = "github/SIES763.MachineLearning/homework/data/CellDNA.csv"
data1 <- read.csv(file=file_name, header=FALSE, sep= ",")
#attach(data1) #can call variables without using $ sign and refernce the datasource.
#stats
#dim(data1)
#names(data1)
#data1

#---------Standarizing nums-----------#
data1$V1 = scale(data1$V1)
data1$V2 = scale(data1$V2)
data1$V3 = scale(data1$V3)
data1$V4 = scale(data1$V4)
data1$V5 = scale(data1$V5)
data1$V6 = scale(data1$V6)
data1$V7 = scale(data1$V7)
data1$V8 = scale(data1$V8)
data1$V9 = scale(data1$V9)
data1$V10 = scale(data1$V10)
data1$V11 = scale(data1$V10)
data1$V12 = scale(data1$V12)
data1$V13 = scale(data1$V13)

#------------Convert y to binary ----------------#
#data1$V14[data1$V14 >= 1] <- 1
data1$V14[data1$V14 >= 1] <- 1  

#------------Convert y to categorical-----------#
data1$V14 = as.factor(data1$V14)

#---------------Create x and y values----------#
x = subset(data1, select = -V14)
y = data1$V14

#---------------Create Model------------------#
model <- svm(x, y) 
#print(model)
#summary(model)

#------------Creating decision values---------#
pred <- predict(model, x, decision.values = TRUE)


#----------Question for homework-------------#
#Question 1: How many support vectors did you find? 536
summary(model) 
#Number of Support Vectors:  311


#Question 2: List top 3 records that have 
            #the smallest **absolute** values 
            #from wT · X + b calculation.

sort(abs(model[["decision.values"]]))[1:3]
#[1] 0.0004653643 0.0019767191 0.0026969651

#Question 3:
  #What are the "wT · X + b" values for the 
  #following records: 131, 165, 892, 1057?
model[["decision.values"]][131] #[1] 0.9996738
model[["decision.values"]][165] #[1] -0.7469051
model[["decision.values"]][892] #[1] -1.683784
model[["decision.values"]][1057]#[1] 0.9996626
  #Anything special about those values of these few records?

#group out the values
#plot(cmdscale(dist(data1[,-14])),col = as.integer(data1[,14]),pch = c("o","+")[1:1217 %in% model$index + 1])


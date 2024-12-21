"
Robert Krall
SEIS 763
Assignment 5
"

#-----------Packages Need -------------#
#install.packages("tidyverse")
#library(tidyverse)
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

#example from site:
#https://rstudio-pubs-static.s3.amazonaws.com/198425_010cec82017b4598a683be5122e53e85.html
#model = svm(data1$V14~., data=data1)


pred = predict(model, x)
#check out accuracy
table(pred, data1$V14)

#compare decisiion values adn prob
pred <- predict(model, x, decision.values = TRUE)
pred
attr(pred, "decision.values")[1:13,]
#visualize 
plot(cmdscale(dist(data1[,-14])),col = as.integer(data1[,14]),pch = c("o","+")[1:1217 %in% model$index + 1])

########

















#----Split between training & validate data----#
assignment = sample(1:2, size = nrow(data1), prob = c(0.5, 0.5), replace = TRUE)
training_data = data1[assignment == 1, ]    
validate_data = data1[assignment == 2, ] 






#-------------Create SVM model --------------#
#svm_model <- svm(V14~ ., data=data1, method="C-classification", kernel="radial")
#svm_model <- svm(V14~ ., data=training_data, kernel="radial")
svm_model <- svm(V14~ ., data=data1, kernel="radial", scale=FALSE))
#svm_model <- svm(V14~ ., data=data1, kernel="linear", cost=10, scale=FALSE)
print(svm_model)
plot(svm_model, x)



svm_predict <-predict(svm_model,data1, decision.values = TRUE, probability = TRUE)
attr(svm_predict, "decision.values")[1:13,]
attr(svm_predict, "probabilities")[1:13,]


X = subset(data1, select = -V14)
y = V14
model = svm(x, V14, probability =TRUE)

data1$V14


sort(abs(svm_predict))







plot(V1,cols=y+1)
xgrid=expand.grid(X1=V1, X2= V2, X3= V3)
plot(xgrid,cols=y+1)



summary(svm_model)



#----Create X and y values ----#
X = subset(data1, select = -V14)
y = V14







model = svm(X,y, probability = TRUE)
summary(model)








#training set predictions
pred_train <-predict(svm_model,training_data)
mean(pred_train==training_data$V14)
pred_train[131]
#validate set predictions
pred_val <-predict(svm_model,validate_data)
mean(pred_val==validate_data$V14)



#---create x and y values----------#
x = data1[1:13]
y = data1[14]








model <- svm(x,y)

#Question 1: How many support vectors did you find? 536
print(model)
summary(model)



  
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

#admin stuff
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
data1$V11 = scale(data1$V11)
data1$V12 = scale(data1$V12)
data1$V13 = scale(data1$V13)

#-----Convert y to binary ----------#
data1$V14[data1$V14 >= 1] <- 1  
#-----Convert y to categorical------#
#data1$V14 = as.factor(data1$V14)

#---create x and y values----------#
x = data1[1:13]
y = data1[14]
model <- svm(x,y)

#Question 1: How many support vectors did you find? 536
print(model)
summary(model)



  
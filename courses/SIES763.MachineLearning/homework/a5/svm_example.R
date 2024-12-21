
#example from this site:
#https://eight2late.wordpress.com/2017/02/07/a-gentle-introduction-to-support-vector-machines-using-r/


#load required library
library(e1071)

#load built-in iris dataset
data(iris)


#set seed to ensure reproducible results
set.seed(42)

#split into training and test sets
assignment = sample(1:2, size = nrow(iris), prob = c(0.5, 0.5), replace = TRUE)

#separate training and test sets
trainset = iris[assignment == 1, ]    
testset  = iris[assignment == 2, ] 

#get column index of train flag
#trainColNum <- grep("train",names(trainset))

#remove train flag column from train and test sets
#trainset <- trainset[,-trainColNum]
#testset <- testset[,-trainColNum]

#get column index of predicted variable in dataset
typeColNum <- grep("Species",names(iris))

#build model - linear kernel and C-classification (soft margin) with default cost (C=1)
svm_model <- svm(Species~ ., data=trainset, method="C-classification", kernel="linear")
svm_model

#training set predictions
pred_train <-predict(svm_model,trainset)
mean(pred_train==trainset$Species)
#test set predictions
pred_test <-predict(svm_model,testset)
mean(pred_test==testset$Species)

"
Robert Krall
SEIS 763
Assignment 6
"

#-----------Packages Need -------------#
#install.packages("e1071")
#install.packages("caret")
#install.packages("plotROC")
#install.packages("pROC")
library(e1071)
library(caret)
library(plotROC)
library(ggplot2)
library(pROC)
library(ROCR)

#-----------Read File In----------------#
file_name = "github/SIES763.MachineLearning/homework/data/CellDNA.csv"
data1 <- read.csv(file=file_name, header=FALSE, sep= ",")

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
X = subset(data1, select = -V14)
y = data1$V14

#---------------Create Model------------------#
svm_mdl <- svm(X, y, kernel='radial') 
#[PredictedClasses, scores] = 
#predict(svm_mdl , X);
confusionMatrix(y, predict(svm_mdl))

predict <- predict(svm_mdl, X, decision.values = TRUE)

prediction <- prediction( predict@predictions, predict@labels)
perf <- performance(prediction,"tpr","fpr")
plot(perf)


ctrl <- trainControl(method="cv",
                     number = 13,
                     summaryFunction=twoClassSummary,
                     classProbs=TRUE)

svm.tune <- train(x=X,
                  y= y,
                  method = "svmRadial",
                  metric="ROC",
                  tuneGrid = grid,
                  trControl=ctrl)

pred <- predict(svm_mdl, X, type="prob")[2]
pred_val <-prediction(pred, y)






svm_mdl <- svm(X, y, kernel='radial') 
prediction_class <- predict(svm_mdl, X)
CFM =confusionMatrix(y, prediction_class)


print(CFM)

precision <- CFM$byClass['Pos Pred Value']  
recall <- CFM$byClass['Sensitivity']
f_measure <- 2 * ((precision * recall) / (precision + recall))
perf1 <- performance(pred, "sens", "spec")
plot(perf1)



#print(CFM)
accuracy = sum(C(CFM))
  
  #sum(diag(CFM,nrow=length(CFM)))#/sum(CFM(1))


diag(v,nrow=length(v))


svm_mdl = fitcsvm(X, Y, 'Standardize', true)
[PredictedClasses, scores] = predict(svm_mdl , X);
CFM = confusionmat(Y, PredictedClasses)
accuracy = sum(diag(CFM))/sum(CFM(:)),






pred <- predict(svm_mdl, X, decision.values = TRUE)

pred_ROCR <- prediction(y,predict(svm_mdl))


roc_ROCR <- performance(pred, measure = "tpr", x.measure = "fpr")
plot(roc_ROCR, main = "ROC curve", colorize = T)
abline(a = 0, b = 1)

pred <- predict(svm_mdl, X, "prod")







fit <- rpart(Kyphosis ~ Age + Number + Start, data = kyphosis)
predict(svm_mdl, type = "prob")   # class probabilities (default)
predict(svm_mdl, type = "vector") # level numbers
predict(svm_mdl, type = "class")  # factor
predict(svm_mdl, type = "matrix") # level number, class frequencies, probabilities


#output confusion matrix for model
confusionMatrix(y, predict(svm_mdl))

table(pred,data1$V14)


pred.svm <- prediction(svm_mdl,X)



roc.perf = performance(svm_mdl, measure = "tpr", x.measure = "fpr")
plot(roc.perf)
abline(a=0, b= 1)

#1. What is the accuracy, Precision, and Recall for each class prediction?
#2. Create an ROC curve plot for each class prediction





svm_mdl = fitcsvm(X, Y, 'Standardize', true)
[PredictedClasses, scores] = predict(svm_mdl , X);
CFM = confusionmat(Y, PredictedClasses)
accuracy = sum(diag(CFM))/sum(CFM(:)),




roc_obj <- roc(x, y)
auc(roc_obj)





category <- c(1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0)
prediction <- rev(seq_along(category))
prediction[9:10] <- mean(prediction[9:10])
library(pROC)
roc_obj <- roc(category, prediction)
auc(roc_obj)
roc_df <- data.frame(
  TPR=rev(roc_obj$sensitivities), 
  FPR=rev(1 - roc_obj$specificities), 
  labels=roc_obj$response, 
  scores=roc_obj$predictor)

roc_df <- transform(roc_df, 
                    dFPR = c(diff(FPR), 0),
                    dTPR = c(diff(TPR), 0))
rectangle <- function(x, y, width, height, density=12, angle=-45, ...) 
  polygon(c(x,x,x+width,x+width), c(y,y+height,y+height,y), 
          density=density, angle=angle, ...)

roc_df <- transform(roc_df, 
                    dFPR = c(diff(FPR), 0),
                    dTPR = c(diff(TPR), 0))

with(roc_df, {
  mapply(rectangle, x=FPR, y=0,   
         width=dFPR, height=TPR, col="green", lwd=2)
  mapply(rectangle, x=FPR, y=TPR, 
         width=dFPR, height=dTPR, col="blue", lwd=2)
  
  lines(FPR, TPR, type='b', lwd=3, col="red")
})

svmmodel.predict<-predict(svmmodel,subset(y,select=x),decision.values=TRUE)


svmmodel.accuracy<-prop.correct(model.confusion)


ctrl <- trainControl(method="cv", 
                     summaryFunction=twoClassSummary, 
                     classProbs=T,
                     savePredictions = T)
rfFit <- train(data1$V14 ~ ., data=data1, 
               method="svmRadial", preProc=c("center", "scale"), 
               trControl=ctrl)



#----------Question for homework-------------#
#Question 1: How many support vectors did you find? 536
summary(model) 
#Number of Support Vectors:  228


#Question 2: List top 3 records that have 
            #the smallest **absolute** values 
            #from wT · X + b calculation.

sort(abs(model[["decision.values"]]))[1:3]
#[1] 0.001103556 0.004214812 0.004297818

#Question 3:
  #What are the "wT · X + b" values for the 
  #following records: 131, 165, 892, 1057?
model[["decision.values"]][131] #[1] 21.4564
model[["decision.values"]][165] #[1] -9.299386
model[["decision.values"]][892] #[1] -4.577076
model[["decision.values"]][1057]#[1] 26.60004
  #Anything special about those values of these few records?
  #These four records are extremely far away from the svm line.



#group out the values
#plot(cmdscale(dist(data1[,-14])),col = as.integer(data1[,14]),pch = c("o","+")[1:1217 %in% model$index + 1])
#install.packages('readxl')
#install.packages('glmnet')
#install.packages('glmnetUtils')
#install.packages('plotmo')
#install.packages('Metrics')
#install.packages('ROCR')
library(readxl)
library(glmnet)
library(glmnetUtils)
library(plotmo)
library(Metrics)
library(ROCR)

#GPS <- read_excel("github/SIES763.MachineLearning/project/data/GPSRetention_with_Dummies.xlsx")
GPS <- read_excel("github/SIES763.MachineLearning/project/data/GPSRetention_Dummies.xlsx")

GPS$`Retained` = as.factor(GPS$`Retained`)
GPS = GPS[,-1:-5]
"
GPS$OUTCOME_NUMBER = scale(GPS$OUTCOME_NUMBER)
GPS$CREDITS_ATTEMPTED = scale(GPS$CREDITS_ATTEMPTED)
GPS$CREDITS_EARNED = scale(GPS$ CREDITS_EARNED)
GPS$GPA = scale(GPS$GPA)
"

assignment = sample(1:2, size = nrow(GPS), prob = c(0.5, 0.5), replace = TRUE)
trainingdata = GPS[assignment == 1, ]    
validatedata = GPS[assignment == 2, ] 


lasso = glmnet(`Retained`~., trainingdata, alpha = 1, family = 'binomial')

plot_glmnet(lasso, label=TRUE)

cv = cv.glmnet(`Retained`~., trainingdata, alpha = 1, nfolds = 10, family = 'binomial')

plot(cv)

coef(cv, s = 'lambda.1se')
coef(cv, s = 'lambda.min')

cv$lambda.1se
cv$lambda.min

lasso_pred = predict(lasso, validatedata[1:74], s = cv$lambda.min, type=c("response"))

auc_lasso = auc(actual = validatedata$`Retained`, predicted = lasso_pred)

auc_lasso

pred = prediction(lasso_pred, validatedata$`Retained`)
roc = performance(pred, "tpr", "fpr")
plot(roc)


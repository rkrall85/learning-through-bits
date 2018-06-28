"
Created By: Quint Sander
Created On: 06/26/2018
Purpose: A script to create models for ML group project

Updated On | Updated By | Purpose
06/28/2018    RTK         Added comments and more desc vars to understand code better.

"
#-----------Packages Need -------------#
    #Install
"
install.packages('readxl')
install.packages('glmnet')
install.packages('glmnetUtils')
install.packages('plotmo')
install.packages('Metrics')
install.packages('ROCR')
"
    #Import
library(readxl)
library(glmnet)
library(glmnetUtils)
library(plotmo)
library(Metrics)
library(ROCR)

#-----------Read File In----------------#
GPS <- read_excel("github/SIES763.MachineLearning/project/data/GPSRetention_with_Dummies.xlsx")
#dim(GPS) #dimension of file 9Rows X Columns)
#Renaming last column so it doesnt have a ? ; that is scewing up variables with attached function
names(GPS)[length(names(GPS))] <- "RETAINED"
names(GPS)[6] <- "TOOK_NON_GPS_COURSE_WITHIN_YEAR"
names(GPS) #read header
attach(GPS) #create a workspace with all variables so you dont have to use $ sign

#-------Remove unwainted Columns-------#
" we dont want to use these columns since these are predictors for once you are in the program.
  we dont see much value for them now.
"
GPS = GPS[,-1:-5]
"
  [1] Fake_ID
  [2] OUTCOME_NUMBER                                         
  [3] CREDITS_ATTEMPTED
  [4] CREDITS_EARNED
  [5] GPA
"

#----------Set up Dummmies-------------#
#not need in this proejct since the file already has dummy vars set up

#---------Standarizing nums-----------#
#No need to do this since we removed their columns
"
  GPS$OUTCOME_NUMBER = scale(GPS$OUTCOME_NUMBER)
  GPS$CREDITS_ATTEMPTED = scale(GPS$CREDITS_ATTEMPTED)
  GPS$CREDITS_EARNED = scale(GPS$ CREDITS_EARNED)
  GPS$GPA = scale(GPS$GPA)
"

#-----Y value (what are we predicting)----#
#RETAINED = as.factor(RETAINED) #what does factor do?
GPS$`RETAINED` = as.factor(GPS$`RETAINED`)


#---------------Sample Data -------#
#breaking the data up between training_data and validate data
assignment = sample(1:2, size = nrow(GPS), prob = c(0.5, 0.5), replace = TRUE)
training_data = GPS[assignment == 1, ]    
validate_data = GPS[assignment == 2, ] 


#---------Lasso Model ------------#
#helps us find the good variables or predictors to use
#lasso_fit = glmnet(training_data,RETAINED, alpha = 1, family = 'binomial')
lasso_fit = glmnet(`RETAINED`~., training_data, alpha = 1, family = 'binomial')
plot_glmnet(lasso_fit, label=TRUE)
#------Lasso Plot with CV---------#
cv = cv.glmnet(RETAINED, training_data, alpha = 1, nfolds = 10, family = 'binomial')
plot(cv)



#output 1 SD from lamdbda value
coef(cv, s = 'lambda.1se') #all matching predictors
cv$lambda.1se  #the value used

coef(cv, s = 'lambda.min')




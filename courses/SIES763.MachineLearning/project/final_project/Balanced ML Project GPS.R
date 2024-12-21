# read in the data
GPS <- read_excel("<REPLACEME>")

# convert the response variable to a factor
GPS$Retained = as.factor(GPS$Retained)

# randomly assign the data to either the trainingdata or validatedata
assignment = sample(1:2, size = nrow(GPS), prob = c(0.5, 0.5), replace = TRUE)
trainingdata = GPS[assignment == 1, ]    
validatedata = GPS[assignment == 2, ] 

# sample down class 1 in the trainingdata to create a balanced dataset
trainingdata = downSample(x = trainingdata[, -84],
                                 y = trainingdata$Retained) 
# recover the correct columnnames
colnames(trainingdata) <- colnames(validatedata)

# scale the CLEANED_PREVIOUS_GPA variable in both datasets
trainingdata$CLEANED_PREVIOUS_GPA=scale(trainingdata$CLEANED_PREVIOUS_GPA)
validatedata$CLEANED_PREVIOUS_GPA=scale(validatedata$CLEANED_PREVIOUS_GPA)

# measure starttime of Logistic Regression
lasso_starttime = Sys.time()

# create Lasso model and plot for Logistic Regression
lasso = glmnet(Retained~., trainingdata, alpha = 1, family = 'binomial')

plot_glmnet(lasso, label=TRUE)

# create Cross-validation model and plot for Logistic Regression
cv = cv.glmnet(Retained~., trainingdata, alpha = 1, nfolds = 10, family = 'binomial')

plot(cv)

coef(cv, s = 'lambda.min')

# measure endtime of Logistic Regression
lasso_endtime = Sys.time()

# use Logistic Regression model to make predictions
lasso_pred = predict(lasso, validatedata, s = cv$lambda.min, type=c("response"))

# calculate AUC for Logistic Regression
auc_lasso = auc(actual = validatedata$Retained, predicted = lasso_pred)

# create Confusion Matrix for Logistic Regression
lasso_cm = confusionMatrix(as.factor(ifelse(lasso_pred > 0.5, 1, 0)), as.factor(validatedata$Retained))

# calculate F-value for class 0 for Logistic Regression
lasso_f0 = (2*lasso_cm$table[1,1])/(2*lasso_cm$table[1,1]+lasso_cm$table[1,2]+lasso_cm$table[2,1])

# calculate F-value for class 1 for Logistic Regression
lasso_f1 = (2*lasso_cm$table[2,2])/(2*lasso_cm$table[2,2]+lasso_cm$table[1,2]+lasso_cm$table[2,1])

# calculate Accuracy for Logistic Regression
lasso_acc = (lasso_cm$table[1,1]+lasso_cm$table[2,2])/sum(lasso_cm$table)

# measure starttime of GBM
gbm_starttime = Sys.time()

# set the Cross-validation parametre to 10-fold
ctrl = trainControl(method = "cv", number = 10, classProbs = TRUE)

# train a Cross-validated GBM model based on highest Accuracy
gbm = train(ifelse(Retained == 1, "yes", "no")~., trainingdata, method = "gbm", metric = "Accuracy", trControl = ctrl)

# measure endtime of GBM
gbm_endtime = Sys.time()

# use GBM model to make predictions
gbm_pred = predict(gbm, validatedata, type="prob")

# calculate AUC for GBM
auc_gbm = auc(actual = validatedata$Retained, predicted = gbm_pred$yes)

# create Confusion Matrix for GBM
gbm_cm = confusionMatrix(as.factor(ifelse(gbm_pred[,'yes'] > 0.5, 1, 0)), as.factor(validatedata$Retained))

# calculate F-value for class 0 for GBM
gbm_f0 = (2*gbm_cm$table[1,1])/(2*gbm_cm$table[1,1]+gbm_cm$table[1,2]+gbm_cm$table[2,1])

# calculate F-value for class 1 for GBM
gbm_f1 = (2*gbm_cm$table[2,2])/(2*gbm_cm$table[2,2]+gbm_cm$table[1,2]+gbm_cm$table[2,1])

# calculate Accuracy for GBM
gbm_acc = (gbm_cm$table[1,1]+gbm_cm$table[2,2])/sum(gbm_cm$table)

# set the Cross-validation parameter to 10-fold
ctrl = trainControl(method = "cv", number = 10, classProbs = TRUE)

# measure starttime of SVM
svm_starttime = Sys.time()

# train a Cross-validated SVM model based on highest Accuracy
svm = train(ifelse(Retained == 1, "yes", "no")~., trainingdata, method = "svmLinear", scale = FALSE, metric = "Accuracy", trControl = ctrl)

# measure endtime of SVM
svm_endtime = Sys.time()

# use SVM model to make predictions
svm_pred = predict(svm, validatedata, type="prob")

# calculate AUC for SVM
auc_svm = auc(actual = validatedata$Retained, predicted = svm_pred$yes)

# create Confusion Matrix for SVM
svm_cm = confusionMatrix(as.factor(ifelse(svm_pred[,'yes'] > 0.5, 1, 0)), as.factor(validatedata$Retained))

# calculate F-value for class 0 for SVM
svm_f0 = (2*svm_cm$table[1,1])/(2*svm_cm$table[1,1]+svm_cm$table[1,2]+svm_cm$table[2,1])

# calculate F-value for class 1 for SVM
svm_f1 = (2*svm_cm$table[2,2])/(2*svm_cm$table[2,2]+svm_cm$table[1,2]+svm_cm$table[2,1])

# calculate Accuracy for SVM
svm_acc = (svm_cm$table[1,1]+svm_cm$table[2,2])/sum(svm_cm$table)

# measure starttime of Random Forest
rf_starttime = Sys.time()

# set the Cross-validation parametre to 10-fold
ctrl = trainControl(method = "cv", number = 10, classProbs = TRUE)

# train a Cross-validated Random Forest model based on highest Accuracy
rf = train(ifelse(Retained == 1, "yes", "no")~., trainingdata, method = "rf", metric = "Accuracy", trControl = ctrl)

# measure endtime of Random Forest
rf_endtime = Sys.time()

# use Random Forest model to make predictions
rf_pred = predict(rf, validatedata, type="prob")

# calculate AUC for Random Forest
auc_rf = auc(actual = validatedata$Retained, predicted = rf_pred$yes)

# create Confusion Matrix for Random Forest
rf_cm = confusionMatrix(as.factor(ifelse(rf_pred[,'yes'] > 0.5, 1, 0)), as.factor(validatedata$Retained))

# calculate F-value for class 0 for Random Forest
rf_f0 = (2*rf_cm$table[1,1])/(2*rf_cm$table[1,1]+rf_cm$table[1,2]+rf_cm$table[2,1])

# calculate F-value for class 1 for Random Forest
rf_f1 = (2*rf_cm$table[2,2])/(2*rf_cm$table[2,2]+rf_cm$table[1,2]+rf_cm$table[2,1])

# calculate Accuracy for SVM
rf_acc = (rf_cm$table[1,1]+rf_cm$table[2,2])/sum(rf_cm$table)

# connect to H2O cluster
h2o.init()

# convert trainingdata to H2O-dataframe
train = as.h2o(GPS[assignment == 1,])

# measure starttime of H2O
h2o_starttime = Sys.time()

# run the automl function for 60 seconds to create several models
aml = h2o.automl(y = 'Retained', training_frame = train, nfolds = 10, max_runtime_secs = 60, balance_classes = TRUE)

# measure endtime of H2O
h2o_endtime = Sys.time()

# print the leaderboard of all H2O models
aml@leaderboard

# use the best H2O model to make predictions
h2o_pred = h2o.predict(aml@leader, as.h2o(GPS[assignment == 2,]))

# convert the predictions from a H2O-object to a matrix
h2o_pred = as.matrix(h2o_pred$p1)

# calculate AUC of the H2O model
auc_h2o = auc(actual = validatedata$Retained, predicted = h2o_pred)

# create Confusion Matrix of the H2O model
h2o_cm = confusionMatrix(as.factor(ifelse(h2o_pred > 0.5, 1, 0)), as.factor(validatedata$Retained))

# calculate F-value of class 0 of the H2O model
h2o_f0 = (2*h2o_cm$table[1,1])/(2*h2o_cm$table[1,1]+h2o_cm$table[1,2]+h2o_cm$table[2,1])

# calculate F-value of class 1 of the H2O model
h2o_f1 = (2*h2o_cm$table[2,2])/(2*h2o_cm$table[2,2]+h2o_cm$table[1,2]+h2o_cm$table[2,1])

# calculate Accuracy of the H2O model
h2o_acc = (h2o_cm$table[1,1]+h2o_cm$table[2,2])/sum(h2o_cm$table)

# print the runtimes of all models
lasso_endtime - lasso_starttime
svm_endtime - svm_starttime
rf_endtime - rf_starttime
gbm_endtime - gbm_starttime
h2o_endtime - h2o_starttime

# print the confusion matrices of all models
lasso_cm$table
svm_cm$table
rf_cm$table
gbm_cm$table
h2o_cm$table

# print the accuracy of all models
sprintf("Logistic Regression Accuracy: %.3f", lasso_acc)
sprintf("SVM Accuracy: %.3f", svm_acc)
sprintf("Random Forest Accuracy: %.3f", rf_acc)
sprintf("GBM Accuracy: %.3f", gbm_acc)
sprintf("H2O Accuracy: %.3f", h2o_acc)

# print the f-scores for both classes for all models
sprintf("Logistic Regression F0: %.3f", lasso_f0)
sprintf("Logistic Regression F1: %.3f", lasso_f1)
sprintf("SVM F0: %.3f", svm_f0)
sprintf("SVM F1: %.3f", svm_f1)
sprintf("Random Forest F0: %.3f", rf_f0)
sprintf("Random Forest F1: %.3f", rf_f1)
sprintf("GBM F0: %.3f", gbm_f0)
sprintf("GBM F1: %.3f", gbm_f1)
sprintf("H2O F0: %.3f", h2o_f0)
sprintf("H2O F1: %.3f", h2o_f1)

# print the AUC scores for both classes for all models
sprintf("Logistic Regression AUC: %.3f", auc_lasso)
sprintf("SVM AUC: %.3f", auc_svm)
sprintf("Random Forest AUC: %.3f", auc_rf)
sprintf("GBM AUC: %.3f", auc_gbm)
sprintf("H2O AUC: %.3f", auc_h2o)

# create a list of all the predictions for the positive classes of all models
preds_list = list(lasso_pred[,1], svm_pred$yes, rf_pred$yes, gbm_pred$yes, h2o_pred[,1])

## create a list with all the test data times the amount of models
m = length(preds_list)
actuals_list = rep(list(validatedata$Retained), m)

# create a list of predictions for all models
pred = prediction(preds_list, actuals_list)

# create an ROC plot for the positive class with all the models included
rocs_y = performance(pred, "tpr", "fpr")
plot(rocs_y, col = as.list(1:m), main = "Test Set ROC Curves for Class 1")
legend(x = "bottomright", 
       legend = c("Logistic Regression", "SVM", "Random Forest", "GBM", "H2O"),
       fill = 1:m)

# create an ROC plot for the negative class with all the models included
rocs_y = performance(pred, "tnr", "fnr")
plot(rocs_y, col = as.list(1:m), main = "Test Set ROC Curves for Class 0")
legend(x = "bottomright", 
       legend = c("Logistic Regression", "SVM", "Random Forest", "GBM", "H2O"),
       fill = 1:m)


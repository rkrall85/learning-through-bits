
%Robert Krall
%SEIS763 
%Assignment 3

%% ================ Part 1: Load Data ================%
load patients 
%enable parallel processing
opt = statset('UseParallel',true);

%% ================ Part 2: Normalize Data ================%
%only going to normalize none cat fields
X = [Age, Height, Weight];
%normalize/standardize (use built zscore funcation or my own)
[X,mu,sigma] = zscore(X);

y = Systolic;


%% ================ Part 3: Linear Regression Model ================%
lrm = fitlm(patients,'ResponseVar','Systolic','PredictorVars', ...
            {zscore('Age'), 'Gender', 'Height', 'Weight', 'Smoker', 'Location','SelfAssessedHealthStatus'},  ...
            'CategoricalVar',{'Gender','Location','SelfAssessedHealthStatus'});
 

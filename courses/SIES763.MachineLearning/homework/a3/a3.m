%{
    Robert Krall
    6/13/2018
    SEIS 763 - Assignment 3
%}

%load data
load patients

opt = statset('UseParallel',true);

%% ================ Part 1: Dummy Variables ================%
gender_group = nominal(Gender);
dummy_gender = dummyvar(gender_group);

location_group = nominal(Location);
dummy_location = dummyvar(location_group);

health_group = nominal(SelfAssessedHealthStatus);
dummy_health = dummyvar(health_group);

%C = unique(SelfAssessedHealthStatus);
%% ================ Part 2: Normalize Data ================%
%only going to normalize none cat fields
X = [Age, Height, Weight];
y = Systolic;

%normalize/standardize (use built zscore funcation or my own)
[X,mu,sigma] = zscore(X);

%Adding dummy observations (or columns)
X = [X,dummy_gender(:,end), Smoker,dummy_location, dummy_health];


%% ================ Part 3: Lasso Model ================%
[B,FitInfo] = lasso(X,y,'CV',10,'Options',opt,'Alpha',1,'PredictorNames',{'Age','Height','Weight','Gender_Male','Smoker','Location_CountyGeneralHositpal','Location_StMarysMedicalCenter','Location_VaHospital','HealthStatus_Excellent','HealthStatus_Fair','HealthStatus_Good','HealthStatus_Poor'});
lassoPlot(B, FitInfo, 'PlotType','Lambda','XScale','log');
%graph settings
xlabel('Lambda')
xtickangle(45)
ylabel('Theta')
yticks(-6:3:10)


[Lb, Lfitinfo] = lasso(X, y, 'Alpha', 1, 'Lambda', 0.97);

Lb
Lfitinfo

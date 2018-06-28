
%{
Robert Krall
SEIS 763 - Machine Learning
Assignment 2

%}
load patients 
%gender
gender_group = nominal(Gender);
dummy_gender = dummyvar(gender_group);
%location
location_group = nominal(Location);
dummy_location = dummyvar(location_group);
%Self Assessed Health Status
health_group = nominal(SelfAssessedHealthStatus);
dummy_health = dummyvar(health_group);

%normalize the data
X_pre = [Age, Height, Weight];
X_norm = zscore(X_pre);
X_norm
X = [X_norm,dummy_gender(:,end), Smoker,dummy_location, dummy_health];
%X = [Age,dummy_gender(:,end), Height, Weight, Smoker, dummy_location, dummy_health];

y = Systolic;
%Question 4
lm = fitlm(X, y)
plot(lm)
%X;
%Question 6
plotDiagnostics(lm, 'cookd')
%mean(lm.Diagnostics.CooksDistance)*3
%Question 7
%plotSlice(lm)
%plotResiduals(lm)

plotSlice(lm)


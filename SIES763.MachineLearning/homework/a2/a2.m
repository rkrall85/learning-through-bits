
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
X = [Age,dummy_gender(:,end), Height, Weight, Smoker, dummy_location, dummy_health];
y = Systolic;
%Question 4
lm = fitlm(X, y)
plot(lm)
%Question 6
plotDiagnostics(lm, 'cookd')
%Question 7
plotSlice(lm)



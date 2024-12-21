%load data
load patients 



%% ================ Part 1: Dummy Variables ================%
gender_group = nominal(Gender);
dummy_gender = dummyvar(gender_group);

location_group = nominal(Location);
dummy_location = dummyvar(location_group);

health_group = nominal(SelfAssessedHealthStatus);
dummy_health = dummyvar(health_group);

%% ================ Part 2: Normalize Data ================%
%only going to normalize none cat fields
X = [Age, Height, Weight];
y = Systolic;

%normalize/standardize (use built zscore funcation or my own)
[X mu sigma] = featureNormalize(X);
%X = zscore(X);

%Adding dummy observations (or columns)
X = [X,dummy_gender(:,end), Smoker,dummy_location, dummy_health];

% Add intercept term to X
%X = [ones(m, 1) X];


%% ================ Part 3: Gradient Descent ================%



%lm = fitlm(X, y)
%plot(lm)

%cost function = square error function


%% ================ Funcations ================%
function [X_norm, mu, sigma] = featureNormalize(X)
    %standard variables
    X_norm = X;
    mu    = mean(X);
    sigma = std(X);
    
    indicies = 1:size(X, 2);

    for i = indicies,
        XminusMu  = X(:, i) - mu(i);
        X_norm(:, i) = XminusMu / sigma(i);
    end
end

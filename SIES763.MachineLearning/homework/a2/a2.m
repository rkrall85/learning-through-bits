%% Clear and Close Figures
clear ; close all; clc

%loading packages needed 
pkg load statistics;

%================FUNCATIONS================%
function plotData(x, y, xlabel, ylabel)
  figure; % open a new figure window
  plot(x, y, 'rx','MarkerSize', 10); %Plot the data
  ylabel(ylabel); %Set the y-axis label
  xlabel(xlabel); %set the x-axis label
  end

function [X_norm, mu, sigma] = featureNormalize(X)
  %standard variables
  X_norm = X;
  mu = zeros(1, size(X, 2));
  sigma = zeros(1, size(X, 2));
  %finding mean and std
  mu    = mean(X);
  sigma = std(X);
  indicies = 1:size(X, 2);
  for i = indicies,
    XminusMu  = X(:, i) - mu(i);
    X_norm(:, i) = XminusMu / sigma(i);
  end
end

function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
  m = length(y); % number of training examples
  J_history = zeros(num_iters, 1);
  for iter = 1:num_iters
    h = X * theta;  %calc the hypothesis
    error_vector = h  - y; %calc the error
    theta_change = (alpha .* X'*(error_vector) ./m);
    
    theta = theta - theta_change;
    
    % Save the cost J in every iteration    
    J_history(iter) = computeCostMulti(X, y, theta);
  end
end



function J = computeCostMulti(X, y, theta)
  m = length(y); % number of training examples
  J = 0;
  h = X * theta;  %calc the hypothesis
  error = h  - y; %calc the error
  error_sqr = error.^2; %error of square
  J = sum(error_sqr)/(2*m); %compute J  
  
end
%===============================================================================


%% Load Data
fprintf('Loading data ...\n');
%data = load('patients.csv');
filename = 'patients.csv';
data = csvread(filename,1,0); %skip header with 1,0 parms being passed
%X = data(:, [1 3 4 10 8 6 7]);y = data(:, 9);
X = data(:, [1 4 10 8]);y = data(:, 9);
%X = data(:, 1);y = data(:, 9);
m = length(y); %number of training examples

fprintf('First 10 examples from the dataset: \n');
fprintf(' x = [%.0f %.0f %.0f %.0f ], y = %.0f \n', [X(1:10,:) y(1:10,:)]');
fprintf('Program paused. Press enter to continue.\n');
pause;

%normalize the data 
[X mu sigma] = featureNormalize(X);

%adding a row of 1s to X
X = [ones(m,1), X]; 

fprintf('First 10 examples from the dataset after adding ones column: \n');
fprintf(' x = [%.0f %.0f %.0f %.0f ], y = %.0f \n', [X(1:10,:) y(1:10,:)]');
fprintf('Program paused. Press enter to continue.\n');
pause;

%% ================ Gradient Descent ================
fprintf('Running gradient descent ...\n');
fprintf('Program paused. Press enter to continue.\n');
pause;


lm = fitlm(X,y)
pause;


% Choose some alpha value
num_iters = 1500;
alpha = 0.03;
[m,n] = size(X); %getting size of X


% Init Theta and Run Gradient Descent
theta = zeros(n, 1);
[theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters);
min(J_history)


% Plot the convergence graph
figure;
plot(1:numel(J_history), J_history, '-b', 'LineWidth', 2);
xlabel('Number of iterations');
ylabel('Cost J');

% Display gradient descent's result
fprintf('Theta computed from gradient descent: \n');
fprintf(' %f \n', theta);
fprintf('\n');



%theta = zeros(n,1); %initialize fitting parameters



% compute initial cost
%fprintf('calc J ...\n');
%J = computeCost(X,y, theta);
%J



%fprintf('First 10 examples from the dataset: \n');
%fprintf(' x = [%.0f %.0f %.0f %.0f %.0f %.0f %.0f], y = %.0f \n', [X(1:10,:) y(1:10,:)]');

% Base, height, weight
%theta = [1;m;7];
#y_hat = theta' * X;
#y_hat(1:10, :)

%X


data = load('ex1data1.txt'); %read in file
x = data(:,1);
y = data(:,2);
m = length(y); %number of training examples

plot(x, y, 'rx', 'MarkerSize', 10); %plot the data
ylabel('Profit of $10,000'); %set the y-axis label
xlabel('Population of City in 10,000s'); %set the x-axis label

X = [ones(m,1), data(:,1)]; %Add a column of ones to x
theta = zeros(2,1); %initialize fitting parameters

iterations = 1500;
alpha = 0.01;


predict1 = [1, 3.5] * theta;


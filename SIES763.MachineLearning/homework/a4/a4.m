%{
Robert Krall
SEIS 763 - Machine Learning
Assignment 4

%}

%load CellDNA
opt = statset('UseParallel',true);

%Step 1: convert table to array and grab X and y values
CellDNA_tbl = table2array(CellDNA);

%Step 2. Getting X and y values
X = CellDNA_tbl(:,1:13);
%convert values to 1 or 0s
y = CellDNA_tbl(:,14);
y(y>0)=1;

%Step 3: Standardize the data
[ZX, me, signma] = zscore(X);

%Step 4: Logistic Regression Algo
lrm = fitglm(ZX, y, 'distr', 'binomial', 'link', 'logit');

p = lrm.Fitted.Response;
Z = lrm.Fitted.LinearPredictor;
figure, gscatter(Z,p, y, 'br');
%plotSlice(lrm)

[B, FitInfo] = lasso(ZX, y, 'CV', 10,'Options', opt, 'Alpha',1);
lassoPlot(B, FitInfo, 'PlotType','Lambda','XScale','log');
%graph settings
xlabel('Lambda')
xtickangle(45)
ylabel('Theta')

[Lb, Lfitinfo] = lasso(ZX, y, 'Alpha', 1, 'Lambda', 0.015);

Lb

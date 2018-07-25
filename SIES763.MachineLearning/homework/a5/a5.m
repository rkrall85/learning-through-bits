%{
Robert Krall
SEIS 763 - Machine Learning
Assignment 5
%}

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

%Step 4: Create SVM model
svm_model = fitcsvm(ZX, y, 'KernelFunction', 'linear', 'Crossval', 'on', 'Standardize', true);

CompactSVMModel = svm_model.Trained{1};
%Question 1: How many support vectors are there? 827
%CompactSVMModel

[label, score] = predict(CompactSVMModel, ZX);

predict_tbl = table(y(1:1217),label(1:1217),score(1:1217,2),'VariableNames',{'TrueLabel','PredictedLabel','Score'});

%Question 2:
%sort(abs(predict_tbl.Score))

%{
    0.0030
    0.0049
    0.0268
%}

%Question 3: Find score for records: 131, 165, 892, 1057
%predict_tbl(131,:)  %  -0.99966
%predict_tbl(165,:)  %  0.27399
%predict_tbl(892,:)  %  0.42265
%predict_tbl(1057,:) %  -1


CFM = confusionmat(y, label)
accuracy = sum(diag(CFM))/sum(CFM(:)),


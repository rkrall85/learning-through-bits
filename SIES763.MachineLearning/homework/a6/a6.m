%{
Robert Krall
SEIS 763 - Machine Learning
Assignment 6
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
svm_mdl = fitcsvm(ZX, y, 'KernelFunction', 'RBF', 'Standardize', true);

[PredictedClasses, scores] = predict(svm_mdl, ZX);
CFM = confusionmat(y,  PredictedClasses);
accuracy = sum(diag(CFM))/sum(CFM(:));

CFM
%1
f1_recall = CFM(1,1)/(CFM(1,1)+CFM(1,2));
f1_precision = CFM(1,1)/(CFM(1,1)+CFM(2,1));

f1_recall
f1_precision
%0
f2_recall = CFM(2,2)/(CFM(2,2)+CFM(2,1));
f2_precision = CFM(2,2)/(CFM(2,2)+CFM(1,2));

f2_recall
f2_precision

%ROC Curves
[xpos, ypos, T, AUC0] = perfcurve(y, scores(:, 1), 0);
figure,     plot(xpos, ypos)
xlim([-0.05 1.05]), ylim([-0.05 1.05])
xlabel('\bf FP rate'),  ylabel('\bf TP rate')
title('\bf ROC for class 0by SVM')


[xpos, ypos, T, AUC1] = perfcurve(y, scores(:, 2), 1);
figure,     plot(xpos, ypos)
xlim([-0.05 1.05]), ylim([-0.05 1.05])
xlabel('\bf FP rate'),  ylabel('\bf TP rate')
title('\bf ROC for class 1by SVM')

library(e1071)

# Read in the csv file
dna <- read.csv("~/Desktop/SEIS 763/CellDNA.csv", header=FALSE)

# Change all non-zero variables for y variable to 1
dna$V14[dna$V14 > 0] <- 1

# Convert y variable to factor
dna$V14 = as.factor(dna$V14)

# Standardize the numerical variables
dna$V1 = scale(dna$V1)
dna$V2 = scale(dna$V2)
dna$V3 = scale(dna$V3)
dna$V4 = scale(dna$V4)
dna$V5 = scale(dna$V5)
dna$V6 = scale(dna$V6)
dna$V7 = scale(dna$V7)
dna$V8 = scale(dna$V8)
dna$V9 = scale(dna$V9)
dna$V10 = scale(dna$V10)
dna$V11 = scale(dna$V11)
dna$V12 = scale(dna$V12)
dna$V13 = scale(dna$V13)


# Create SVM model
svm_model = svm(V14~., dna)

# Print summary stats
summary(svm_model)

# Sort the absolute Wt * X + b values by values
sort(abs(svm_model$decision.values))
# Sort the absolute Wt * X + b values by record number
sort(abs(svm_model$decision.values), index.return = TRUE)

# Look up values of specific records
svm_model$decision.values[131,]
svm_model$decision.values[165,]
svm_model$decision.values[892,]
svm_model$decision.values[1057,]




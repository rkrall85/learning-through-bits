patients <- read.csv("~/Desktop/SEIS 763/patients.csv")
X = patients[,-2]
X = X[,-4]
X$Age =scale(X$Age)
X$Weight =scale(X$Weight)
X$Height =scale(X$Height)
fit = lm(Systolic~., X)
summary(fit)
cooksd = cooks.distance(fit)
plot(cooksd, col="lightblue", pch=19, cex=2)
text(cooksd, labels=rownames(X), cex=0.9, font=2)


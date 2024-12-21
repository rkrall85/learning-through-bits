
cor(mlb11$runs, mlb11$at_bats)
plot(mlb11$runs ~ mlb11$new_obs)

plot_ss(x = mlb11$at_bats, y = mlb11$runs)
plot_ss(x = mlb11$at_bats, y = mlb11$runs, showSquares = TRUE)
m1 <- lm(runs ~ at_bats, data = mlb11)
summary(m1)
m2 <-lm(homeruns ~ runs, data=mlb11) #Question 3
summary(m2) #Question 3
abline(m2)

plot(mlb11$runs ~ mlb11$at_bats)
abline(m1)

plot(m1$residuals ~ mlb11$at_bats)
abline(h = 0, lty = 3) # adds a horizontal dashed line at y = 0

qqnorm(m1$residuals)
qqline(m1$residuals) # adds diagonal line to the normal prob plot
savehistory(file = "Assign8.Rhistory")
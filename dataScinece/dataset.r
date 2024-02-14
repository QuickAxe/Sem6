# using inbuilt iris dataset:
test = iris

# structure of test:
str(test)


minWidth <- min(test$Sepal.Width)
minLength <- min(test$Sepal.Length)
minpWidth <- min(test$Petal.Width)
minpLength <- min(test$Petal.Length)

maxWidth <- max(test$Sepal.Width)
maxLength <- max(test$Sepal.Length)
maxpWidth <- max(test$Petal.Width)
maxpLength <- max(test$Petal.Length)

range <- function(x) {
    m <- max(x) - min(x)
    return(m)
}

range(test$Sepal.Length)
range(test$Sepal.Width)
range(test$Petal.Length)
range(test$Petal.Width)

mean(test$Sepal.Length)
mean(test$Sepal.Width)
mean(test$Petal.Length)
mean(test$Petal.Width)

median(test$Sepal.Length)
median(test$Sepal.Width)
median(test$Petal.Length)
median(test$Petal.Width)

mode <- function(x) {
    t <- sort(table(x), decreasing = TRUE)[[1]]
    return(t)
}

mode(test$Sepal.Length)
mode(test$Sepal.Width)
mode(test$Petal.Length)
mode(test$Petal.Width)

"---------------------------"
quantile(test$Sepal.Length, 0.25)
quantile(test$Sepal.Length, 0.50)
quantile(test$Sepal.Length, 0.75)
quantile(test$Sepal.Length, 1)
"---------------------------"
quantile(test$Sepal.Width, 0.25)
quantile(test$Sepal.Width, 0.50)
quantile(test$Sepal.Width, 0.75)
quantile(test$Sepal.Width, 1)
"---------------------------"
quantile(test$Petal.Length, 0.25)
quantile(test$Petal.Length, 0.50)
quantile(test$Petal.Length, 0.75)
quantile(test$Petal.Length, 1)
"---------------------------"
quantile(test$Petal.Width, 0.25)
quantile(test$Petal.Width, 0.50)
quantile(test$Petal.Width, 0.75)
quantile(test$Petal.Width, 1)

# inter quantile value
IQR(test$Sepal.Length)
IQR(test$Sepal.Width)
IQR(test$Petal.Length)
IQR(test$Petal.Width)

#  standard deviation
sd(test$Sepal.Length)
sd(test$Sepal.Width)
sd(test$Petal.Length)
sd(test$Petal.Width)

"---------------------"
# variance
var(test$Sepal.Length)
var(test$Sepal.Width)
var(test$Petal.Length)
var(test$Petal.Width)

"---------------------"
# all quantile values
summary(test$Sepal.Length)
summary(test$Sepal.Width)
summary(test$Petal.Length)
summary(test$Petal.Width)

"---------------------"
# corellation
cor(test$Sepal.Length, test$Sepal.Width)
cor(test$Petal.Length, test$Petal.Width)

# plots
barplot(test$Sepal.Length)
barplot(test$Sepal.Width)
barplot(test$Petal.Length)
barplot(test$Petal.Width)

boxplot(test$Sepal.Length)
boxplot(test$Sepal.Width)
boxplot(test$Petal.Length)
boxplot(test$Petal.Width)

boxplot(test$Sepal.Length ~ test$Species)

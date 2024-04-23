products <- data.frame(
    ProductId = c(101, 102, 103),
    ProductName = c("T-Shirt", "Jeans", "Shoes"),
    Price = c(15.99, 20.99, 49.98),
    Stock = c(50, 30, 25),
    stringsAsFactors = FALSE
)
print(products)

# print first column of dataframe
products[1]

# structure of dataframe
str(products)


# summary of dataframe
b = summary(products)
b

# accessing the same attribute using different methods:-------------------------
result = data.frame(products$ProductName)
result

products[1]

products[["ProductName"]]

products$Price

dim(products)

# adding a new row:
newProduct = c(104, "SunGlasses", 39.99, 40)
products = rbind(products, newProduct)
cat("\nUpdated product dataframe:\n")
products

# adding a new column

Discount <- c(5, 10, 8, 4)
products <- cbind(products, Discount)
products

# combining two dataframes into one

products1 <- data.frame(
    ProductId = c(105, 106),
    ProductName = c("Belt", "Trousers"),
    Price = c(20.99, 45.98),
    Stock = c(70, 40),
    Discount = c(10, 15),
    stringsAsFactors = FALSE
)
products1

combined = rbind(products, products1)
combined

# now horizontally

products3 <- data.frame(Brand = c("Noke", "Abbibas", "OverArmour", "Mucci", "Louis Bitton", "Divided Colours of Menetton"))

combined1 <- cbind(combined, products3)
combined1

"=================================================================================================================================================================="

# ==============================================================================
# install.packages("dplyr")
library(dplyr)

stats <- data.frame(
    player = c("a", "b", "c", "d", "a", "a"),
    runs = c(100, 200, 408, 19, 56, 100),
    wickets = c(17, 20, NA, 5, 2, 17)
)

# fetch players who scored more than 100 runs
filter(stats, runs > 100)

filter(stats, wickets > 10)

# remove duplicates:
# reove duplicate rows, but the whole row must match:
distinct(stats)

# remove duplicate columns:
distinct(stats, player, .keep_all = TRUE)

# arrange the thing
arrange(stats, runs)
arrange(stats, wickets)

# fetch required column data:
select(stats, player, wickets)

# rename:
rename(stats, runsScored = runs)

# add new column, based on existing columns:
mutate(stats, avg = runs / 4)

# drop all and create a new column
transmute(stats, avg = runs / 4)

summarise(stats, sum(runs), mean(runs))

# horizontal bar plot
barplot(as.double(products$Price), main = "Price of products", xlab = "price", horiz = TRUE)

hist(as.double((products$Stock), main = "Product stock", xlab = "Stock", xlim = c(0, 100), col = "green"))

boxplot(as.double(products$Price), horizontal = TRUE, main = "Price", xlab = "Rupees", ylab = "Price", col = "orange", border = "brown")


products$Price = as.double(products$Price)
products$Stock = as.double(products$Stock)
boxplot(products[, 3:4], main = "box plots for products")

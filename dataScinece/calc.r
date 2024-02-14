cat("Enter values of a and b: \n")

a <- as.integer(readLines("stdin", n = 1))
b <- as.integer(readLines("stdin", n = 1))

cat("Enter : \n1. a+b\n2. a-b\n3. a*b\n4. a/b\n5. a%b\n6. a^b")
choice <- readLines("stdin", n = 1)

result <- switch(choice,
    "1" = paste("sum=", a + b),
    "2" = paste("difference=", a - b),
    "3" = paste("product=", a * b),
    "4" = paste("quotient=", a / b),
    "5" = paste("remainder=", a %% b),
    "6" = paste("power=", a**b),
    "Wrong Choice"
)

cat(result)
cat("\n\n")

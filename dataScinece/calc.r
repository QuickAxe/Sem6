cat("Enter values of a and b: \n")

a <- as.numeric(readLines("stdin", n = 1))
b <- as.numeric(readLines("stdin", n = 1))

cat(
    "Enter operation: \n",
    "1. a + b\n",
    "2. a - b\n",
    "3. a * b\n",
    "4. a / b\n",
    "5. a %% b\n",
    "6. a^b\n",
    "7. sqrt(a)\n",
    "8. log(a, b)\n",
    "9. sin(a)\n",
    "10. cos(a)\n",
    "11. tan(a)\n",
    "12. exp(a)\n",
    "13. a^2\n",
    "14. a^3\n",
    "15. a^(1/2)\n",
    "16. a^(1/3)\n",
    "17. log10(a)\n",
    "18. log2(a)\n",
    "19. factorial(a)\n",
    "20. abs(a - b)\n"
)

choice <- as.integer(readLines("stdin", n = 1))

result <- switch(choice,
    "1"  = paste("sum=", a + b),
    "2"  = paste("difference=", a - b),
    "3"  = paste("product=", a * b),
    "4"  = paste("quotient=", a / b),
    "5"  = paste("remainder=", a %% b),
    "6"  = paste("power=", a^b),
    "7"  = paste("square root of a=", sqrt(a)),
    "8"  = paste("logarithm base b of a=", log(a, b)),
    "9"  = paste("sine of a=", sin(a)),
    "10" = paste("cosine of a=", cos(a)),
    "11" = paste("tangent of a=", tan(a)),
    "12" = paste("exponential of a=", exp(a)),
    "13" = paste("a^2=", a^2),
    "14" = paste("a^3=", a^3),
    "15" = paste("square root of a=", a^(1 / 2)),
    "16" = paste("cube root of a=", a^(1 / 3)),
    "17" = paste("log base 10 of a=", log10(a)),
    "18" = paste("log base 2 of a=", log2(a)),
    "19" = paste("factorial of a=", factorial(a)),
    "20" = paste("absolute difference between a and b=", abs(a - b)),
    "Wrong Choice"
)

cat(result)
cat("\n\n")

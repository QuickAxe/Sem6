lung <- read.csv("./dataScinece/LungCapData.txt", sep = "\t")
# lung
dim(lung)
str(lung)

# lung[1:2]

head(lung)
tail(lung)

# View(lung)


lung1 <- read.table("./dataScinece/LungCapData.txt", sep = "\t", header = TRUE)
# lung1

write.table(lung, "lungCapData1.csv", sep = ",")

con <- file("./lungCapData1.csv", "r")

lung2 = readLines(con)
lung2[2]

sample = c("rollNo, name, age, class", "101, A, 21, T6")
writeLines(sample, "sample.csv")

s <- data.frame(102, "B", 33, "T1000")
names(s) <- c("rollNo", "name", "age", "class")

sample2 = read.csv("./sample.csv")
w1 <- rbind(sample2, s)

barplot(lung$LungCap)

boxplot(lung$LungCap)

data = read.csv('hw1_data.csv', header=TRUE)
sub_set = subset(data, Ozone > 31 & Temp > 90)
means <- apply(sub_set, 2, function(x) mean(x, na.rm=TRUE))
print(means)
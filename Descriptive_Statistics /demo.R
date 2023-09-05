###Table 1

## creating a data frame

data_table = data.frame(col1=sample(6:9,9,replace=TRUE),col2=letters[1:3],col3=c(1,4,1,2,2,2,1,2,2))
print('Original Dataframe')
print(data_table)

print('Modified Frequecy Table')
freq=table(data_table$col1)
print(freq)
mean(freq)
median(freq)
mode(freq)

print('Cumulative Frequency Table')
cumsum=cumsum(freq)
print(cumsum)


print('Relative Frequency Table')
prob=prop.table(freq)

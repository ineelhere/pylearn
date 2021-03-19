#reduce and lambda combination
#Syntax for reduce = reduce(function,sequence)
#Syntax for lambda = lambda lambda_arguements:expression

#code to find sum of all items in a list 
from functools import reduce
mylist = [10,20,30,40,50]
sumlist = reduce(lambda m,n:m+n, mylist)
print(sumlist)

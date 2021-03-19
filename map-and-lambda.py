#map and lambda combination
#Syntax for map = map(function,iteration)
#Syntax for lambda = lambda lambda_arguements:expression

#code to find whether items in a list are even or odd
mylist = [33,554,24234,23423424,44,5534]
evenodd = list(map(lambda n: "Odd" if (n%2==1) else "even", mylist))
print(evenodd)

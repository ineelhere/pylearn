# fibonacci series using recursive function
def fibo(n):
    return n if n<=1 else fibo(n-1)+fibo(n-2)
n = int(input("Please enter the number for the fibonacci series - " ))
print("Here is the series")
for n in range(n):
    print(fibo(n))

# finding factorial of a number using recursive function
def facto(n):
    return 1 if n==1 else (n*facto(n-1))
n = int(input("Please enter the number for calculating factorial - " ))
facto(n)

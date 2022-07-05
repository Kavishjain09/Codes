#M-1
def fact(num):
    n=1
    for i in range(1, num+1):
           n*=i
    return n
print(fact(4))


#M-2
def factorial(n):
     if (n==1 or n==0):

        return 1

     else:

        return (n * factorial(n - 1))

print("Factorial : ",factorial(5))

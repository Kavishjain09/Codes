def check_strong_number(num):
    temp=num
    sum=0
    while(temp>0):
        n=1
        k=temp%10
        for i in range(1,k+1):
            n*=i
        print("Factorial of",k,"=",n)
        sum+=n
        temp=temp//10
    print("\n Sum of Factorials of a Given Number %d = %d" %(num, sum))
    return sum
    if (sum == num):
        print(" The given number is a Strong Number")
    else:
        print(" The given number is not a Strong Number")
input=145
print(check_strong_number(input))

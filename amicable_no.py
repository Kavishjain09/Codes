def amicable(a,b):
    sum1=0
    for i in range(1,(a//2)+1):
        if a%i==0:
            sum1+=i
    sum2=0
    for i in range(1,(b//2)+1):
        if b%i==0:
            sum2+=i
    if sum1==b and sum2==a:
        print(a,b," are amicable numbers")
    else:
        print(a," and ",b," are numbers are not amicable")
amicable(220,284)
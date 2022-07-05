num=int(input("Enter any no. to find the fibonacci of first n no. : "))
f0=0
f1=1
f2=1
for i in range(0, num+1):
    if(i==0):
        print(str(i) + "  " + str(0))
    elif(i==1):
        print(str(i) + "  " + str(1))
    else:
        f1=f2
        f2=f0 + f1
        f0=f1
        print(str(i) + "  " + str(f2))

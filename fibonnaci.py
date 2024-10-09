num=int(input("Enter any no. to find the fibonacci of first n no. : "))
f1=0
f2=1
print("0" + "  " + str(f1))
for i in range(1, num):
    print(str(i) + "  " + str(f2))
    next=f1+f2
    f1=f2
    f2=next

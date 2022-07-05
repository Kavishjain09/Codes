num=int(input("Enter the number :"))
if(num%3==0):
    if(num%5==0):
        print("Zoom")
    else:
        print("Zip")
elif(num%5==0):
    print("Zap")
else:
    print("Invalid")

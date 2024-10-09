a = 2
b = 200
for i in range(a,b+1):
    for j in range(a, (i//2)):
        if(i%j==0):
            break
    else:
        print(i)

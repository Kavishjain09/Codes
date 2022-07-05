a = 100
b = 200
count=0
for i in range(a,b):
    for j in range(2, i//2):
        if(i%j==0):
            break
    else:
        count+=1
        if (count%2!=0):
            print(i)

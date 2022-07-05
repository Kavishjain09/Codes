list=[1,1,5,100,-20,-20,6,0,0]
count=0
for i in range(0,len(list)):
    if(list[i]==list[i-1]):
        count+=1
    else:
        continue
print(count)

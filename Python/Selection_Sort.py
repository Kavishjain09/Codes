def sort():
    for i in range(len(data)-1):
        minpos=i
        for j in range(i,len(data)):
            if data[minpos]>data[j]:
                minpos=j
        temp=data[i]
        data[i]=data[minpos]
        data[minpos]=temp
data=[8,3,7,6,5,2]
sort()
print(data)

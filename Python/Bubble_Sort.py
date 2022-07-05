def sort():
    for i in range(len(data)-1,0,-1):
        for j in range(i):
            if data[j]>data[j+1]:          #Swapping consecutive number
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
data=[8,3,7,6,5,2]
sort()
print(data)

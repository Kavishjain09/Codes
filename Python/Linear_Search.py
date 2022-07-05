def search(data,n):
    i=0
    while i< len(data):
        if data[i]==n:
            globals()['v']= i
            return True
        i=i+1
    return False
data=[4,7,3,5,8,2]
n=3
if search(data,n):
    print("found at position",v+1)
else:
    print("not found")

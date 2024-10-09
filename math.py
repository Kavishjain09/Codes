def 
n,m,a=int(input())
count=0
if n<a and m<a:
    print(count+1)
elif n<a or m<a:
    if len(n)>len(m):
        for i in range(n):
            count+=1
    else:
        for i in range(m)
def Hcf(n,m):
    A=[]
    for i in range(2,n+1):
        if n%i==0 and m%i==0:
            A.append(i)
    # return max(A)
    if len(A)==1:
        return A[0]
    if len(A)>1:
        t=A[0]
        for i in range(len(A)-1):
            if t<A[i+1]:
                t=A[i+1]
        return t
print(Hcf(35,105))
print(Hcf(15,50))
print(Hcf(15,30))

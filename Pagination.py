A=[]
def pagination(A,page,limit):
    B=[]
    C=[]
    for i in range(1,101):
        A.append(i)
    if page==1:
        for i in range(1,limit+1):
            B.append(i)
        return B
    else:
        for i in range(page*limit,page*limit+limit+1):
            C.append(i)
        return C
print(pagination(A,6,4))
print(pagination(A,5,10))
print(pagination(A,9,5))

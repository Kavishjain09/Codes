C=[]
def fun(A,B):
    if len(A)==len(B):
        for i in range(len(A)):
            C.append((A[i]))
            C.append(B[i])
        return C
    elif len(A)>len(B):
        for i in range(len(A)):
            C.append(A[i])
            if i<len(B):
                C.append(B[i])
        return C
    else:
        for i in range(len(B)):
            if i<len(A):
                C.append(A[i])
            C.append(B[i])
        return C
A = [1,4,6,9,12]
B = ["a","b","c","d","e"]
print(fun(A,B))
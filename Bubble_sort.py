A=[
[4,2],
[4,-2],
[-3,5],  
[0,5],
[-2,-4],
[-2,-1],
[-1,5],
[-1,2],
[0,-2],
[0,5],
[-3,-2],
]
B=[]
C=[]
D=[]
def Bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(0,len(A)-i-1):
            if A[j][0]==A[j+1][0]:
                if A[j][1]>A[j+1][1]:
                    A[j], A[j+1]= A[j+1], A[j]
            elif A[j][0]>A[j+1][0]:
                A[j], A[j+1]= A[j+1], A[j]
    return A
print(Bubble_sort(A))







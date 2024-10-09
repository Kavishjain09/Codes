A=[1,2,3,4,5,6,7,8]
def chunk(A,chunk_num):
    for i in range(chunk_num,len(A)+chunk_num,chunk_num):
        B=[]
        for j in range(i-chunk_num,i):
            if j<len(A):
                B.append(A[j])
        print(B)
chunk(A,3)
chunk(A,5)

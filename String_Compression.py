def String_Compression(S):
    r=""
    i=1
    count=1

    while i< len(S):
        if S[i]==S[i-1]:
            count+=1
        else:
            r=r+ S[i-1]+ str(count)
            count=1
        i+=1
    r=r+S[i-1] + str(count)
    return r
print(String_Compression("AAb"))
#input: "this is my laptop"
#output: "laptop my is this"
#also remove leading and trailing spaces
def S_rev(s):
    words=[]
    rev=[]
    for word in s.split():
        words.append(word)
    for i in range(len(words)-1,-1,-1):
        rev.append(words[i])
    return " ".join(rev)
print(S_rev("This is my Laptop"))

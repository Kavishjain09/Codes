def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
list =[20,25,14,19,53,63,44,56]
even,odd=count(list)
print("Even : {} and Odd : {}".format(even,odd))

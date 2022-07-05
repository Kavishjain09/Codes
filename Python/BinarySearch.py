def binary_Search(list,key):
    first =0
    last=len(list)-1
    while first<=last and not found:
        middle=(first+last)//2
        if list[middle]==key:
            return True
        else:
            if key<list[middle]:
                last=middle
            else:
                first=middle
list=[4,7,8,12,45,99]
print(binary_Search(list,7))

def bin_no(alist,key):
    if len(alist)>0:
        mid = len(alist) //2
        if key==alist[mid]:
            return True

        if key<alist[mid]:
            return bin_no(alist[:mid],key)

        if key>alist[mid]:
            return bin_no(alist[mid+1:],key)
    else:
        return False
print(bin_no([10,20,30,40,50],40))

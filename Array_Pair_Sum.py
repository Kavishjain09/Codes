#print sum of all unique pairs of array of ([1,3,2,2],4)
#i.e. (1,3)
#     (2,2)
def Pair_sum(arr,k):
    if len(arr)<2:
        return
    seen = set()
    output= set()
    for i in arr:
        target=k-i
        if target not in seen:
            seen.add(i)
        else:
            output.add((min(i,target),max(i,target)))
    print("\n".join(map(str,output)))
Pair_sum([1,3,2,2],4)
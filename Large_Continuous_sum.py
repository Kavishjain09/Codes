def large_Cont_sum(arr):
    max_sum=current_sum=arr[0]
    for num in arr[1:]:
        current_sum=max(current_sum+num,num)
        max_sum=max(current_sum,max_sum)
    return max_sum
print(large_Cont_sum([1,-10,-2,3]))
print(large_Cont_sum([1,2,-1,3,4,10,10,-10,-1]))
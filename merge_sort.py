# Merge Sort

def merge_sort(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=(left[i:])
    result+=(right[j:])
    return result

def merge(arr):
    if len(arr)<=1:
        return arr
    else:
        l=len(arr)//2
        left=merge(arr[:l])
        right=merge(arr[l:])
        return merge_sort(left,right)

arr=[43,23,64,12,66]
print(merge(arr))

# SELECTION SORT

def selection_sort(arr):  # FUNCTION DEFINITION
    n=len(arr)  # STORING LENGTH IN THE VARIABLE
    for i in range(n-1):  # RUNNING FOR LOOP TILL THE RANGE N-1
        min_idx=i  # SETTING THE MINIMUM INDEX TO I
        for j in range(i+1,n): # RUNNING ANOTHER LOOP FOR COMPARISON
            if arr[j]<arr[min_idx]:  # COMPARING THE CURRENT ELEMENT WITH THE MIN_IDX ELEMENT
                min_idx=j  # SETTING THE MIN IDX TO J IF THE CONDITION SATISFIES
        arr[i],arr[min_idx]=arr[min_idx],arr[i]  # SWAPPING
    return arr  # RETURNING THE ARRAY 
print(selection_sort([2,3,1,4]))  # PRINTING AND CALLING THE FUNCTION
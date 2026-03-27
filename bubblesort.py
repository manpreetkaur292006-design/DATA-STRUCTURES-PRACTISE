# BUBBLE SORT

def bubble_sort(arr): # DEFINING THE FUNCTION

    n=len(arr)  # STORING LENGTH IN A VARIABLE

    for i in range(n):  # FOR LOOP TILL THE RANGE N

        for j in range(0,n-i-1):  # FOR LOOP TILL THE RANGE N-I-1
            
            if arr[j]>arr[j+1]:  # COMPARING THE ELEMENTS

                arr[j],arr[j+1]=arr[j+1],arr[j]  # SWAPPING
                
    return arr  # RETURNING THE OUTPUT

print(bubble_sort([3,1,4,2]))  # PRINTING THE OUTPUT AND CALLING THE FUNCTION
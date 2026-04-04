# Heap Sort

# COMPLETE WORKING CODE
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):  # ← Takes array, sorts it in-place
    n = len(arr)
    
    # Phase 1: Build heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Phase 2: Extract max repeatedly
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        heapify(arr, i, 0)               # Re-heapify

# HOW TO CALL IT:
arr = [64, 34, 25, 12, 22, 11, 90]
heap_sort(arr)  # ← Just pass your array!
print(arr)      # [11, 12, 22, 25, 34, 64, 90]
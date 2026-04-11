# Counting Sort

def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1  # Number of possible values
    
    # Step 1: Count frequencies
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1  # Offset for non-zero min
    
    # Step 2: Make cumulative
    for i in range(1, range_size):
        count[i] += count[i-1]
    
    # Step 3: Build result (backwards for stability)
    result = [0] * len(arr)
    for i in range(len(arr)-1, -1, -1):
        pos = count[arr[i] - min_val] - 1  # Position to place
        result[pos] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return result

# Test it!
arr = [2, 2, 0, 3, 2]
print(counting_sort(arr))  # [0, 2, 2, 2, 3] ✅
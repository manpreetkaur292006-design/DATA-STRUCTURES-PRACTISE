# Bucket Sort

def bucket_sort(arr):
    if not arr:
        return arr
    
    n = len(arr)
    # Create n empty buckets
    buckets = [[] for _ in range(n)]
    
    # Step 1: Put elements into buckets
    for num in arr:
        # For floats [0,1): bucket_index = int(n * num)
        # For integers 0..max: bucket_index = int((num/max_val) * (n-1))
        bi = int(n * num)  # Assumes input in [0,1)
        buckets[bi].append(num)
    
    # Step 2: Sort individual buckets (small lists → Insertion Sort perfect)
    for bucket in buckets:
        bucket.sort()  # or insertion_sort(bucket)
    
    # Step 3: Concatenate all buckets
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1
    
    return arr

# Test it!
arr = [0.12, 0.81, 0.33, 0.09]
print(bucket_sort(arr))  # [0.09, 0.12, 0.33, 0.81]
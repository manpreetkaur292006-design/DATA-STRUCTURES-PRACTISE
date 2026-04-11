# Radix Sort

def count_sort_for_radix(arr, exp):  # exp = 1, 10, 100...
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits 0-9
    
    # Count occurrences of current digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    # Cumulative
    for i in range(1, 10):
        count[i] += count[i-1]
    
    # Build result (backwards)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    
    # Copy back
    for i in range(n):
        arr[i] = output[i]


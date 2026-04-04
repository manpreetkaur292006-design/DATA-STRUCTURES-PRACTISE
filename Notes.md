| Algorithm | Status | Key Insight         |
| --------- | ------ | ------------------- |
| Bubble    | ✅      | Adjacent swaps      |
| Selection | ✅      | 1 swap/pass         |
| Insertion | ✅      | Shifts 0 to i-1     |
| Merge     | ✅      | Split + merge       |
| Quick     | ✅      | Partition + recurse |
|Heap       | ✅      | Build MAX_HEAP + extract max + repeat|


## heap-sort
heapify(arr, n, i):
- Assume i is largest
- Check children 2i+1, 2i+2  
- If child > parent → swap + recurse ✓
- Maintains: parent ≥ children ✓

Build phase: n//2-1 → 0 (non-leaves only) ✓
Extract phase: swap root→end + heapify(0) ✓

but technically these two functions are void functions (they sort in-place and return nothing).
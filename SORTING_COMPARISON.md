## **COMPLETE SORTING ALGORITHMS COMPARISON** 📊

Here's the **detailed master table** of all **9 sorting algorithms**:

| **Algorithm** | **Best** | **Average** | **Worst** | **Space** | **Stable** | **In-place** | **Best Use Case** |
|---------------|----------|-------------|-----------|-----------|------------|--------------|-------------------|
| **Bubble Sort** | O(n) | **O(n²)** | **O(n²)** | O(1) | ✅ Yes | ✅ Yes | Tiny arrays (<10), educational |
| **Selection Sort** | O(n²) | **O(n²)** | **O(n²)** | O(1) | ❌ No | ✅ Yes | Few swaps needed, simple |
| **Insertion Sort** | O(n) | **O(n²)** | **O(n²)** | O(1) | ✅ Yes | ✅ Yes | **Nearly sorted data**, small arrays |
| **Merge Sort** | **O(n log n)** | **O(n log n)** | **O(n log n)** | **O(n)** | ✅ Yes | ❌ No | Linked lists, guaranteed performance |
| **Quick Sort** | O(n log n) | **O(n log n)** | **O(n²)** | O(log n) | ❌ No* | ✅ Yes | **General purpose**, cache-friendly |
| **Heap Sort** | **O(n log n)** | **O(n log n)** | **O(n log n)** | O(1) | ❌ No | ✅ Yes | When memory is tight |
| **Counting Sort** | **O(n+k)** | **O(n+k)** | **O(n+k)** | O(n+k) | ✅ Yes | ❌ No | **Small range integers** (0-100) |
| **Radix Sort** | **O(d(n+k))** | **O(d(n+k))** | **O(d(n+k))** | O(n+k) | ✅ Yes | ❌ No | **Large integers** (IDs, 0-1M) |
| **Bucket Sort** | **O(n+k)** | **O(n)** | **O(n²)** | O(n) | ✅ Yes* | ❌ No | **Uniform distribution** (floats) |

_*Quick Sort can be stable with extra work. Bucket Sort stability depends on inner sort._

## **Visual Performance Ranking** 🏁

```
1.  Counting Sort    → O(n+k)  [k small]
2.  Bucket Sort      → O(n)    [uniform data]  
3.  Radix Sort       → O(d(n+k)) [reasonable digits]
4.  Merge/Quick/Heap → O(n log n)
5.  Insertion        → O(n²) but adaptive
6.  Bubble/Selection → O(n²) always
```

## **Memory Usage Ranking** 💾

```
✅ BEST (O(1)): Heap, Bubble, Selection, Insertion
⚠️  Medium (O(log n)): Quick Sort  
❌ Worst (O(n)): Merge, Counting, Radix, Bucket
```

## **When to Use Each (Real-World)** 🌍

```
Educational/Tiny arrays:     Bubble, Selection, Insertion
General purpose:             Quick Sort (default choice)
Guaranteed speed:            Merge Sort  
Memory-tight:                Heap Sort
Small range (0-100):         Counting Sort
Large integers (IDs):        Radix Sort  
Uniform floats [0,1):        Bucket Sort
Nearly sorted:               Insertion Sort
```

## **Level Of Difficulty** 🎯
```
🟢 EASY: Bubble/Selection/Insertion/Counting (you aced these)
🟡 MEDIUM: Merge/Quick/Heap/Radix/Bucket (you understood deeply) 

```

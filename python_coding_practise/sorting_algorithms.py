# =============================================================================
# SORTING ALGORITHMS
# =============================================================================


# =============================================================================
# 1 BUBBLE SORT
# Time Complexity
# worst case O(n²)
# average Θ(n^2)
# best Ω(n)
# Space complexity O(1)
# =============================================================================

def bubble_sort(n):
    for i in range(len(n)):
        swapped = False
        for j in range(len(n)-1-i):
            if n[j]>n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                swapped = True
            if not swapped:
                break


# =============================================================================
# 2 SELECTION SORT
# Time Complexity: best/average/worst O(n^2)
# Space complexity O(1)
# =============================================================================

def selection_sort(n):
    for i in range(len(n)):
        minim = i
        for j in range(i+1, len(n)):
            if n[j]<n[minim]:
                minim = j
        n[j], n[j+1] = n[j+1], n[j]




# =============================================================================
# 3 INSERTION SORT
# Time Complexity
# worst case O(n²)
# average Θ(n^2)
# best Ω(n)
# Space complexity O(1)
# =============================================================================


def insertion_sort(n):
    for i in range(len(n)):
        key = n[i]
        pos = i
        while pos > 0 and n[pos - 1] > key:
            n[pos] = n[pos - 1]
            pos = pos - 1
        # Break for the final swap
        n[pos] = key
    return n


# =============================================================================
# 4 MERGE SORT: Divide and Conquer
# Time Complexity: best/average/worst (n log(n))
# Space complexity O(n)
# =============================================================================

def merge_sort(n):
   if len(n)>1:
       mid = len(n)//2
       lefthalf = n[:mid]
       righthalf = n[mid:]

       #recursion
       merge_sort(lefthalf)
       merge_sort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               n[k]=lefthalf[i]
               i=i+1
           else:
               n[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           n[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           n[k]=righthalf[j]
           j=j+1
           k=k+1

alist = [54,26,93,17,77,31,44,55,20]
merge_sort(alist)




# =============================================================================
# 5 QUICK SORT: Divide and Conquer (pivot partitioning)
# Time Complexity
# worst case O(n²)
# average Θ(n log(n))
# best Ω(n log(n)) same as merge sort
# Space complexity O(n log(n))
# =============================================================================


def quick_sort(n):
    # 3 partitions
    less = []
    equal = []
    greater = []

    # if partition size is greater than 1
    if len(n) > 1:
        pivot = n[0]  # Select first element as pivot
        for x in n:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return n    



# =============================================================================
# 6 COUNTING SORT
# Time complexity: worst/best/average O(n+k)
# Space complexity: O(k)
# =============================================================================

def counting_sort(arr, exp1): 
    n = len(arr) 

    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1

    # Copying the output array to arr[], so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  


# =============================================================================
# 7 RADIX SORT
# Time complexity: worst/best/average O(nk)
# Space complexity: O(n+k)
# =============================================================================


def radix_sort(arr): 
    max_val = max(arr) 
    exp = 1
    while max_val/exp > 0: 
        counting_sort(arr,exp) 
        exp *= 10

  


# =============================================================================
# 8 BUCKET SORT
# Time Complexity
# worst case O(n²)
# average Θ(n+k)
# best Ω(n+k)
# Space complexity O(n)
# =============================================================================

def bucketSort(x): 
    arr = [] 
    slot_num = 10
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(slot_num): 
        arr[i] = insertion_sort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x



   

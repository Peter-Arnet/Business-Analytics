def recursive_fibonacci(n):
    """
    Assumes that n is an int >= 0
        returns Fibonacci of n
    
    Example use:
    >>> recursive_fibonacci(2)
    1
    >>> recursive_fibonacci(5)
    5
    >>> recursive_fibonacci(8)
    21
    """
    if n == 0: 
        return 0
    elif n == 1:
        return 1        
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


def merge_sort(L):
    """
    Sort the input list using the merge sort algorithm.
    
    Parameters:
        L is an unsorted list
        
    Returns:
        L sorted in increasing order
    
    Examples:
    >>> merge_sort([3, 6, 8, 2, 78, 1, 23, 45, 9])
    [1, 2, 3, 6, 8, 9, 23, 45, 78]
    >>> merge_sort([1 ,13, -23, 2.7, -3, 5, 7.5])
    [-23, -3, 1, 2.7, 5, 7.5, 13]
    """
    if len(L) < 2: # Base case - list is max one item, so sorted
        return L[:] # Return copy of the entire list
    else: # General case: split and sort each half, then merge
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        merged_list = merge(left, right)
        return merged_list


def merge(left, right):
    """
    Merge two sorted lists into one
    
    Parameters: 
        left and right are sorted lists
       
    Returns a single sorted list.
    
    Example use:
    >>> left = [1, 5, 6]
    >>> right = [2, 3, 4]
    >>> merge(left, right)
    [1, 2, 3, 4, 5, 6]
    """
    
    result = [] # the result of merging
    i = 0 # Index for left list
    j = 0 # Index for right list
    
    # Loop through both lists comparing items
    # In each iteration append the smallest item to result
    # Stop loop when one list fully copied
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    # Once one list is fully copied, add the remaining items of the other
    if i == len(left): 
        result = result + right[j:]
    else: 
        result = result + left[i:]
    return result

    


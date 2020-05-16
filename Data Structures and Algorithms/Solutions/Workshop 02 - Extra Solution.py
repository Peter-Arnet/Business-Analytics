def check_sorted(L):
    """
    Uses looping to check whether a list is sorted or not (could be increasing or decreasing).
    Examples:
    >>> check_sorted([3,6,48,24,51,262,119])
    False
    >>> check_sorted([748,623,424,414,74,2])
    True
    >>> check_sorted([1, 2, 3])
    True
    """
    ascending = True
    descending = True
    for i in range(len(L)-1):
        if L[i]<L[i+1]:
            ascending = False		
        if L[i]>L[i+1]:
            descending = False
    return ascending or descending


def longest_sorted(L):
    """
    Returns the longest sorted sequence in a list (ascending).
    Examples:
    >>> longest_sorted([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 13, 15, 3, 11, 7, 5])
    [1, 9, 13, 15]
    >>> longest_sorted([25, 72, 31, 32, 8, 20, 38, 43, 85, 39, 33, 40, 98, 37, 14])
    [8, 20, 38, 43, 85]
    """
    curr_counter = 0
    curr_sequence = []
    max_counter = curr_counter
    max_sequence = curr_sequence
    for i in range(len(L)-1):
        if L[i]<=L[i+1]:
            curr_counter += 1
            curr_sequence.append(L[i])
        else:
            curr_counter += 1
            curr_sequence.append(L[i])
            if curr_counter > max_counter:
                max_counter = curr_counter
                max_sequence = curr_sequence
            curr_counter = 0
            curr_sequence = []

    return max_sequence


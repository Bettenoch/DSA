def has_duplicates(arr):
    """
    Check if there are duplicates in the array.

    Parameters:
    arr (list): The input array.

    Returns:
    bool: True if duplicates are found, otherwise False.
    """
    seen = set()  # Set to store unique elements
    for num in arr:
        
        if num in seen:
            return True  # Duplicate found
        
        seen.add(num)  # Add the number to the set
        
    return False  # No duplicates found

arr = [1, 4, 5, 6]
print (arr[:2+1])
print(has_duplicates(arr))


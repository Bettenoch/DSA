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



def test2(arr=[], word=str):
    final = set()
    for i in range(len(word)):
        for string in arr:
            if string[i] == word[i]:
                final.add(string[i])
    return final
    
arr = ["flower", "flow", "flight"] 
word = "flow"

print(test2(arr, word))   
# print (arr[:2+1])
# print(has_duplicates(arr))


def longest_common_prefix(arr):
    if not arr:  # If the array is empty, return an empty string
        return ""
    
    # Find the shortest string in the array
    shortest = min(arr, key=len)
    
    # Initialize the prefix as the shortest string
    for i in range(len(shortest)):
        # Compare the character in all strings at the current position
        for string in arr:
            if string[i] != shortest[i]:
                # If there's a mismatch, return the prefix up to this point
                return shortest[:i]
    
    # If no mismatch is found, the entire shortest string is the prefix
    return shortest

# Example usage
arr = ["flower", "flow", "flight"]
print(longest_common_prefix(arr))  # Output: "fl"

arr = ["dog", "racecar", "car"]
print(longest_common_prefix(arr))  # Output: ""

def checksum(arry, target):
    n = len(arry)
    
    for i in range(n):
        for j in range(i+1, n):
            if arry[i] + arry[j] == target:
                return True
    return False

def two_sum(arr, target):
    n = len(arr)

    # Iterate through each element in the array
    for i in range(n):
        # For each element arr[i], check every
        # other element arr[j] that comes after it
        for j in range(i + 1, n):
            # Check if the sum of the current pair
            # equals the target
            if arr[i] + arr[j] == target:
                return True
    # If no pair is found after checking all possibilities
    return False



def two_sum_beta(arr, target):
    arr.sort()
    left, right = 0, len(arr)-1
    
    while left < right:
        summ = arr[left] + arr[right]
        
        if summ == target:
            return True
        elif summ > target:
            right -=1
        else:
            left += 1


arry = [1, 2, 3, 4, 5, 6]

target = 7

print(two_sum_beta(arry, target))
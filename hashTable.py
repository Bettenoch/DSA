arr1 = [4,9,6,13, 23,9, 4]
arr2 = [5, 6, 9,8, 23, 0, 6,7]

def getDuplicate(arr1, arr2):
    unique = set(arr1)
    duplicates =[]
    for num in arr2:
        if num in unique and num not in duplicates:
            duplicates.append(num)
    return duplicates
        
result = getDuplicate(arr1, arr2)
print(result)
    
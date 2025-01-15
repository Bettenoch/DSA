def duplicateKDistance(arr, k):
    
    test = arr[:k+1]
    
    present = set()
    
    for num in test:
        if num in present:
            return True
        present.add(num)
    return False

arr = [1, 4, 6, 4, 8, 11, 1]

print(duplicateKDistance(arr, 3))
def duplicate_with_k_distance(arr, k):
    test = arr[:k + 1]

    present = set()

    for num in test:
        if num in present:
            return True
        present.add(num)
    return False


arr2 = [1, 4, 6, 4, 8, 11, 1]

print(duplicate_with_k_distance(arr2, k=3))

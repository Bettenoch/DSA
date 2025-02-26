from typing import Any


def binary_search(arr, item: int) -> Any:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high + low) // 2

        guess = arr[mid]

        if guess == item:
            return mid
        if guess < item:
            low = mid + 1

        else:
            high = mid - 1
        return f"{item}not found"


scores = [1, 5, 7, 14, 88, 13, 2, 34]

print(binary_search(scores, 13))

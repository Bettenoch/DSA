def swap(arr, i, k):
    arr[i], arr[k] = arr[k], arr[i]

def Partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for k in range(low, high):
        if arr[k] < pivot:
            i += 1
            swap(arr, i, k)
            
    swap(arr, i + 1, high)
    return i + 1

def QuickSort(arr, low, high):
    if low < high:
        mid = Partition(arr, low, high)
        QuickSort(arr, low, mid - 1)
        QuickSort(arr, mid + 1, high)

def quicksort(arr):
    QuickSort(arr, 0, len(arr) - 1)
    return arr  # Return the sorted array

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quicksort(arr)  # Call the function
print(sorted_arr)  # Print the sorted array

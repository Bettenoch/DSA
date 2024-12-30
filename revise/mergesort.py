def merge(arr1, arr2):
    
    sorted_array = []
    i = j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1
            
    #merge the remaining arrays
    sorted_array.extend(arr1[i:])
    sorted_array.extend(arr2[j:])
    
    return sorted_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left_array = merge_sort(arr[:mid])
    right_array = merge_sort(arr[mid:])
    
    return merge(left_array, right_array)
    

test_array = [38, 27, 43, 3, 9, 82, 10]

print (merge_sort(test_array))
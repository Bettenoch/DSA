def checkOdd(arr):
    show = []
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            show.append(arr[i])
            
    return show



def checkEven(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        if arr[start] % 2 == 0:
            arr[start], arr[end] = arr[end], arr[start]
            end -= 1
        else:
            start += 1
            
    
    return arr
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result2 = checkEven(arr)



result = checkOdd(arr)
print(result2)
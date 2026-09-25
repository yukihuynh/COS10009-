def binary_search(arr, target):
    left = 0 
    right = len(arr) - 1
    
    while left <= right: 
        mid = (left + right) // 2
        if arr[mid] == target: 
            return mid
        elif arr[mid] < target: 
            left = mid + 1
        else: 
            right = mid - 1

    return -1 

number = [ 1,2,3,4,5,6,7,8]
target_num= binary_search(number, 5 + 1)
print(target_num)

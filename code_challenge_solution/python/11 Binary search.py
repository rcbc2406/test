def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

# Test the function
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 12
result = binary_search(arr, target)

if result != -1:
    print("Element is found at index", str(result))
else:
    print("Element is not found")
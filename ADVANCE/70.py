def binary_search(arr, low, high, target):
    if low > high:
        return -1  

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)  
    else:
        return binary_search(arr, low, mid - 1, target)  

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter the number to search for: "))
result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")

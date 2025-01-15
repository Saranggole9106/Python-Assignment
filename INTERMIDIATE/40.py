def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = sorted(map(int, input("Enter sorted numbers separated by spaces: ").split()))
target = int(input("Enter number to search: "))
index = binary_search(lst, target)
print(f"Number found at index: {index}" if index != -1 else "Number not found.")

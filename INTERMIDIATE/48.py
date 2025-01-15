def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Sum of elements: {recursive_sum(lst)}")

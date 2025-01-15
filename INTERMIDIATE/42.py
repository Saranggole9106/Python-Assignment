def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

lst = list(map(int, input("Enter unique numbers separated by spaces: ").split()))
result = second_largest(lst)
print(f"Second largest element: {result}" if result else "Not enough unique elements.")

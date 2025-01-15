def remove_duplicates(lst):
    return list(set(lst))

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"List without duplicates: {remove_duplicates(lst)}")

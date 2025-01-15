def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

numbers = [1, 2, 3, 4, 5]

result = recursive_sum(numbers)
print(f"The sum of the list is: {result}")

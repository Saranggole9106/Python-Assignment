num_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
min_value, max_value = num_list[0], num_list[0]
for num in num_list:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num
print("Minimum:", min_value)
print("Maximum:", max_value)

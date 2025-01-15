num_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
search_num = int(input("Enter number to count: "))
count = 0
for num in num_list:
    if num == search_num:
        count += 1
print(f"{search_num} appears {count} times.")
num_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
for i in range(len(num_list) // 2):
    num_list[i], num_list[-i-1] = num_list[-i-1], num_list[i]
print("Reversed List:", num_list)
def element_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print(f"Frequency of elements: {element_frequency(lst)}")

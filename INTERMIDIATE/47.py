def demonstrate_set_operations(set1, set2):
    return {
        "Union": set1 | set2,
        "Intersection": set1 & set2,
        "Difference (set1 - set2)": set1 - set2
    }

set1 = set(map(int, input("Enter elements of set1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of set2 separated by spaces: ").split()))

results = demonstrate_set_operations(set1, set2)
for op, res in results.items():
    print(f"{op}: {res}")

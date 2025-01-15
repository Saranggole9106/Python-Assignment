def invert_dict(d):
    return {v: k for k, v in d.items()}

d = eval(input("Enter a dictionary (e.g., {'a': 1, 'b': 2}): "))
print(f"Inverted dictionary: {invert_dict(d)}")

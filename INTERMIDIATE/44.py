def squares_dict(n):
    return {i: i**2 for i in range(1, n + 1)}

n = int(input("Enter a number: "))
print(f"Dictionary of squares: {squares_dict(n)}")

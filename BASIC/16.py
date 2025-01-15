base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = 1
for _ in range(exponent):
    result *= base
print("Result:", result)
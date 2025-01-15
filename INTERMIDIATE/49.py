def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"GCD of {a} and {b}: {gcd(a, b)}")

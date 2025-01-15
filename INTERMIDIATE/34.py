def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print(f"Prime numbers between {start} and {end}: {primes_in_range(start, end)}")

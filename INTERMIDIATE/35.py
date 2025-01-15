def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter a number: "))
print(f"{num} is a palindrome: {is_palindrome(num)}")

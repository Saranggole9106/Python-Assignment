string = input("Enter a string: ")

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count


print("The length of the string is:", string_length(string))

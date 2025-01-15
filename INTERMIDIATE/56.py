def convert_to_int(s):
    try:
        num = int(s)  # Attempt to convert the string to an integer
        return num
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")

# Test the function
user_input = input("Enter a number: ")
result = convert_to_int(user_input)
if result is not None:
    print(f"The integer value is: {result}")

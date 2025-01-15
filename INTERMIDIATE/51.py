file_path = input("Enter the file path to read: ")
try:
    with open(file_path, 'r') as file:  # Open the file in read mode
        contents = file.read()         # Read all the contents
        print("File Contents:\n", contents)  # Print the contents
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")

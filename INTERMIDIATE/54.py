file_path = input("Enter the file path to count lines: ")

try:
    with open(file_path, 'r') as file:  # Open the file in read mode
        lines = file.readlines()        # Read all lines into a list
    print(f"The file contains {len(lines)} lines.")
except FileNotFoundError:
    print("Error: File not found.")

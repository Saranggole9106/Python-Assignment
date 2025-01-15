source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")

try:
    # Open the source file for reading and destination file for writing
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        dest.write(src.read())  # Write the contents of source to destination
    print(f"Contents copied successfully from {source_file} to {destination_file}.")
except FileNotFoundError:
    print("Error: Source file not found.")

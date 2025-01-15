def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read()
        
        with open(destination, 'w') as dest_file:
            dest_file.write(content)
        print(f"Contents copied from {source} to {destination}.")
    except FileNotFoundError:
        print(f"Error: {source} does not exist.")

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
copy_file(source_file, destination_file)

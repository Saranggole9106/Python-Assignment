def search_in_file(filename, substring):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines, 1):
                if substring in line:
                    print(f"Line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print("The file does not exist.")

filename = input("Enter the file name to search: ")
substring = input("Enter the substring to search for: ")
search_in_file(filename, substring)

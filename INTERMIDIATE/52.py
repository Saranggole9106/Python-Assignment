file_name = input("Enter the name of the file to write to: ")
content = input("Enter the text to write into the file: ")

# Open the file in write mode and write the content
with open(file_name, 'w') as file:
    file.write(content)

print(f"Content successfully written to {file_name}.")

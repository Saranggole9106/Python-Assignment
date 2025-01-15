import csv

file_path = input("Enter the path to the CSV file: ")

try:
    with open(file_path, 'r') as file:  # Open the CSV file in read mode
        reader = csv.reader(file)
        for row in reader:  # Iterate through each row
            print(row)  # Print the row
except FileNotFoundError:
    print("Error: CSV file not found.")

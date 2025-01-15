import json
import shutil
import os

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    file_path = "data.json"
    
    # Backup the original file
    if os.path.exists(file_path):
        shutil.copy(file_path, file_path + ".bak")
    
    try:
        data = read_json(file_path)
        print("Original JSON data:")
        print(data)

        while True:
            key_to_modify = input("Enter the key to modify (or 'exit' to quit): ")
            if key_to_modify.lower() == 'exit':
                break
            if key_to_modify in data:
                new_value = input(f"Enter the new value for '{key_to_modify}': ")
                data[key_to_modify] = new_value
            else:
                print(f"Key '{key_to_modify}' not found in the JSON file.")

        write_json(file_path, data)
        print("Updated JSON data written to the file.")

    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON. Please ensure the file is properly formatted.")

if __name__ == "__main__":
    main()
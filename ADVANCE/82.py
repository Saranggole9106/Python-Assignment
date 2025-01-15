def find_longest_word(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            longest_word = max(words, key=len)
            print(f"The longest word in the file is '{longest_word}'.")
    except FileNotFoundError:
        print("The file does not exist.")

filename = input("Enter the file name to find the longest word: ")
find_longest_word(filename)

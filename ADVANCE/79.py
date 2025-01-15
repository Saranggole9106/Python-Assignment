def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"The file contains {len(words)} words.")
    except FileNotFoundError:
        print("The file does not exist.")

filename = input("Enter the file name to count words: ")
count_words_in_file(filename)

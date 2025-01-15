string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for char in string if char in vowels)
print("The number of vowels in the string is:", vowel_count )

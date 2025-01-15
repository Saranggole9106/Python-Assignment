import random

def guess_number():
    target = random.randint(1, 10)
    guess = None
    print("Guess a number between 1 and 10.")
    while guess != target:
        guess = int(input("Your guess: "))
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print("Correct! You guessed it!")

guess_number()

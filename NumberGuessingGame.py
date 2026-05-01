import random

print("Welcome to the Number Guessing Game!")
number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 50: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
        break
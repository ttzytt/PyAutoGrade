import random


secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number between 1 and 10: "))

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")

    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")


import random


target_number = random.randint(1, 10)

print("Guess the number between 1 and 10!")

while True:
    
    guess = int(input("Enter your guess: "))

    
    if guess == target_number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < target_number:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high. Try again!")







import random

random.seed()

guess = int(input('Guess a number 1-10(inclusive): '))
number = random.choice([1 , 2 , 3, 4, 5, 6, 7, 8, 9, 10])


while guess != number:

    if guess > number:
        guess = int(input('Too high! Guess again:'))

    elif guess < number:
        guess = int(input('Too low! Guess again:'))

print("That's correct!")

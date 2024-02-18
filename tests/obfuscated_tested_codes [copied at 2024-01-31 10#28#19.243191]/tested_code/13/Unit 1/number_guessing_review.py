


import random

random.seed()

number = random.randint(1, 10)
guess = int(input('I have an integer from 1-10.  What is my number?'))
while guess != number:
    if guess < number:
        print('Your guess is too low!')
    elif guess > number:
        print('You guess is too high!')
    guess = int(input('What is my number?'))

print('You guessed it!')






'''
This code will let the computer choose a random number between 1 and 10.
Then the user will attempt to guess the number with the computer giving
clues about if the number is higher or lower throughout the guessing.
'''
import random

random.seed()

number = random.randint(1, 10)

guess = int(input('I have an integer from 1-10.  What is my number? '))
print()

while guess != number:
    if guess < number:
        
        print('Your guess is too low!')
        print()
    elif guess > number:
        
        print('You guess is too high!')
        print()
        
    guess = int(input('What is my number? '))
    print()

print('You guessed it!')


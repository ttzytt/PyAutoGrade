


"""
This program lets the user try to guess the random number that the
computer chose, and after each guess the computer says wether the guess
is within 200 of the target number. 
"""

import random

target_number = random.randint(100, 999)


guess = int(input('Guess the three digit number that I am thinking of: '))


while target_number < guess or target_number > guess :

    if 100 <= guess <= 999:
        if guess == target_number:
            print('Congratulations! You guessed the correct number.')
        
        elif guess < target_number:
            
            print('Your guess is too low.')
            if target_number - guess > 200 or target_number - guess < -200:
                
                print('Your guess is more than 200 off')
                print()
                guess = int(input('Guess the three digit number that I am thinking of: '))
                
            else:
                print('Your guess is within 200 of the target number')
                print()
                guess = int(input('Guess the three digit number that I am thinking of: '))
                
        elif guess > target_number:
            print('Your guess is too high.')
            
            if target_number - guess > 200 or target_number - guess < -200:
                print('Your guess is more than 200 off')
                print()
                guess = int(input('Guess the three digit number that I am thinking of: '))

            else:
                print('Your guess is within 200 of the target number')
                print()
                guess = int(input('Guess the three number that I am thinking of: '))
    
    else:  
        print("Please choose a valid number")
        guess = int(input('Guess the three digit number that I am thinking of: '))
        
print('Congratulations! You guessed the correct number.')

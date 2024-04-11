





import random

target_number = random.randint(1, 10)


guess = int(input('Guess the number from 1 to 10 that I am thinking of: '))


while target_number < guess or target_number > guess :

    if 1 <= guess <= 10:
        if guess == target_number:
            print('Congratulations! You guessed the correct number.')
        
        elif guess < target_number:   
            print('Your guess is too low.')
            guess = int(input('Guess the number from 1 to 10 that I am thinking of: '))
        
        elif guess > target_number:
            print('Your guess is too high.')
            guess = int(input('Guess the number from 1 to 10 that I am thinking of: '))
    
    else:  
        print("Please choose a number between 1 and 10.")
        guess = int(input('Guess the number from 1 to 10 that I am thinking of: '))
        
print('Congratulations! You guessed the correct number.')

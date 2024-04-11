



import random

random.seed()


guess_number = random.randint(1, 10) 
print('Guess the number! The number is between 1 and 10.')
guess_input = int(input('Enter your guess: '))


whether_correct = 'No' 
while whether_correct == 'No':
    
    if guess_input == guess_number:
        print('Correct! You get it!')
        whether_correct = 'Yes' 

     
    elif guess_input < guess_number:
        print('Your guess is too low.')
        print() 
        guess_input = int(input('Guess again: '))

    
    else:
        print('Your guess is too high.')
        print() 
        guess_input = int(input('Guess again: '))


        
    


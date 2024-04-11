


import random

computer = ['rock', 'paper', 'scissors']

user_choice = input("Enter 'rock' or 'paper' or 'scissors': ")






computer_choice = random.choice(computer)
print('I choose ' + computer_choice  + '.')




if computer_choice == user_choice:
    print('We tie.')
elif user_choice == 'rock': 
    if computer_choice == 'scissors':
        print('You win.')
    else:  
        print('I win.')

elif user_choice == 'paper':
    if computer_choice == 'scissors':
        print('I win.')
    if computer_choice == 'rock':
        print('You win.')

elif user_choice == 'scissors':
    if computer_choice == 'paper':
        print('You win.')
    if computer_choice == 'rock':
        print('I win.')



    
       






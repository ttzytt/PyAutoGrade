h


import random

computer = ['rock', 'paper']

user_choice = input("Enter 'rock' or 'paper': ")






computer_choice = random.choice(computer)
print('I choose ' + computer_choice  + '.')




if computer_choice == user_choice:
    print('We tie.')
elif user_choice == 'rock' and computer_choice == 'paper':
    print('I win.')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win.')
    










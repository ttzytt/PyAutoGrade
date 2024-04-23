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
    




'''
The user should have a choice between “rock” or “paper”,
and the computer should choose randomly. Here is some sample output:




     Enter 'rock' or 'paper': paper
     I choose rock.
     You win.

        print('Press r for rock)
        print('Press p for paper')
        print('Press s for sciccors')

        if user chioce == 'r'
        return 'rock'

        if user choice == 'p'
        return 'paper'

        if user choice == 's'
        return 'scissors'
    





print('choose rock, paper, or sciccors')
if (choice == random)
then (comp choice)
'''





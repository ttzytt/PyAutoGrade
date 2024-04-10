







from random import choice



user_choice = input('Rock or Paper: ').lower()

computer_choice = choice(['rock','paper'])

print('I choose ' + computer_choice)

if user_choice == 'rock':
    if computer_choice == 'rock':
        print('We tie.')
    elif computer_choice == 'paper':
        print('I win.')
elif user_choice == 'paper':
    if computer_choice == 'rock':
        print('You win.')
    elif computer_choice == 'paper':
        print('We tie.')

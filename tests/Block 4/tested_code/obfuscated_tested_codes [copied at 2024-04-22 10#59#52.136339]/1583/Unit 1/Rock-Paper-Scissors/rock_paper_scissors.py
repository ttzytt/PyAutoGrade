


import random

random.seed()


random_choice = random.randint(0, 2)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'


user_choice = input("Enter 'rock' or 'paper' or 'scissors': ").lower()



print('I choose ' + str(computer_choice) + '.')




if user_choice == 'paper':
    if computer_choice == 'rock':
        print('You win.')
    elif computer_choice == 'scissors':
        print('I win.')
    else:
        print('We tie.')
        

elif user_choice == 'rock':
    if computer_choice == 'scissors':
        print('You win.')
    elif computer_choice == 'paper':
        print('I win.')
    else:
        print('We tie.')


else:
    if computer_choice == 'paper':
        print('You win.')
    elif computer_choice == 'rock':
        print('I win.')
    else:
        print('We tie.')

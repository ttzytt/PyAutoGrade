


import random








random_choice = random.randint(0, 2)


choices = ['rock', 'paper', 'scissors']


user_choice = input("Enter 'rock' or 'paper' or 'scissors': ").lower()


computer_choice = choices[random_choice]


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

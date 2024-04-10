



import random


random_choice = random.randint(0,1)


choices = ['rock', 'paper']


user_choice = input("Enter 'rock' or 'paper': ").lower()


computer_choice = choices[random_choice]


print('I choose ' + str(computer_choice) + '.')


if user_choice == 'paper':
    if computer_choice == 'rock':
        print('You win.')
    else:
        print('We tie.')
else:
    if computer_choice == 'rock':
        print('We tie.')
    else:
        print('I win.')

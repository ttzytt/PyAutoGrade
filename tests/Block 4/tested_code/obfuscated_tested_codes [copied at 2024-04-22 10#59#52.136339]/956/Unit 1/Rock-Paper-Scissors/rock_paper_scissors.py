



import random

random.seed()


Answer = input("Enter 'rock' or 'paper' or 'scissors' ")


computer_choice = random.randint(0,2)




if computer_choice == 0:
    print('I choose rock.')
    if Answer == 'rock':
        print('We tie.')
    elif Answer == 'paper':
        print('You win.')
    else:
        print('I win.')




elif computer_choice == 1:
    print('I choose paper.')
    if Answer == 'rock':
        print('I win.')
    elif Answer == 'paper':
        print('We tie.')
    else:
        print('You win.')




else:
    print('I choose scissors.')
    if Answer == 'rock':
        print('You win.')
    elif Answer == 'paper':
        print('I win.')
    else:
        print('We tie.')

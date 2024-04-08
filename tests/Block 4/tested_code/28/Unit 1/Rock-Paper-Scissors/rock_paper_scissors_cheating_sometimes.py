


import random

random.seed()


user_choice = input("Enter 'rock' or 'paper' or 'scissors': ").lower()


cheating_choice = random.randint(1, 10)


if cheating_choice == 1:
    cheating = True
else:
    cheating = False


if cheating == True:
    if user_choice == 'rock':
        print('I choose paper.')
        print('I win.')

    elif user_choice == 'paper':
        print('I choose scissors.')
        print('I win.')

    elif user_choice == 'scissors':
        print('I choose rock.')
        print('I win.')

    else: 
        print('Invalid answer.')

else: 
    
    random_choice = random.randint(0, 2)

    
    choices = ['rock', 'paper', 'scissors']

    
    computer_choice = choices[random_choice]


    

    
    if user_choice == 'paper':
        print('I choose ' + str(computer_choice) + '.')
        if computer_choice == 'rock':
            print('You win.')
        elif computer_choice == 'scissors':
            print('I win.')
        else:
            print('We tie.')
            
    
    elif user_choice == 'rock':
        print('I choose ' + str(computer_choice) + '.')
        if computer_choice == 'scissors':
            print('You win.')
        elif computer_choice == 'paper':
            print('I win.')
        else:
            print('We tie.')

    
    elif user_choice == 'scissors':
        print('I choose ' + str(computer_choice) + '.')
        if computer_choice == 'paper':
            print('You win.')
        elif computer_choice == 'rock':
            print('I win.')
        else:
            print('We tie.')

    
    else:
        print('Invalid answer.')

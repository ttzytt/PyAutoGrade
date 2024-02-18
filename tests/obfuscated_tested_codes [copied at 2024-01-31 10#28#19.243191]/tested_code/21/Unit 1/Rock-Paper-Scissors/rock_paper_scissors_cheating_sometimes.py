


import random 

random.seed()

player_choice = input("Enter 'rock', 'paper' or 'scissors': ")

random_number = random.randint(1,10)





if random_number == 1: 
    if player_choice == 'rock':
        computer_choice = 'paper'
        print("I choose " + computer_choice + '.')
        print ('I win.')
    

    elif player_choice == 'paper':
        computer_choice = 'scissors'
        print("I choose " + computer_choice + '.')
        print ('I win.')

    elif player_choice == 'scissors':
        computer_choice = 'rock'
        print("I choose " + computer_choice + '.')
        print ('I win.')


else: 
    computer_choice = random.choice(('rock', 'paper', 'scissors'))
    print ("I choose " + computer_choice + ".")
    
    if player_choice == computer_choice:
        print('We tie.')


    elif player_choice == 'rock':
        if computer_choice == 'paper':
            print('I win.')
        elif computer_choice == 'scissors':
            print('You win.')

    elif player_choice == 'paper':
        if computer_choice =='rock':
            print('You win.')
        elif computer_choice == 'scissors':
            print('I win.')

    elif player_choice == 'scissors':
        if computer_choice == 'rock':
            print ('I win.')
        elif computer_choice == 'paper':
            print('You win.')


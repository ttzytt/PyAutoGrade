




import random

random.seed()

print("Welcome to rock paper scissors! Please feel free to enter 'quit' when you want to stop playing.")

player_choice = input("Enter 'rock', 'paper' or 'scissors': ")



while player_choice != 'quit':
    # If the input isn't quit then it will just run normally
    computer_choice = random.choice(('rock', 'paper', 'scissors'))

    print ("I choose " + computer_choice + ".")
    if player_choice == computer_choice:
        print('We tie.')


    if player_choice == 'rock':
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
    

    else:
        print("Silly! That's not rock paper scissors! :(")

    print()
        
    player_choice = input("Enter 'rock', 'paper' or 'scissors': ")



if player_choice == 'quit':
    print('Bye!')








import random


player_input = input('Enter rock, paper, scissors, or quit: ')
random.seed()


while player_input != 'quit':
    
    
    bot_choice = random.choice(['rock', 'paper', 'scissors'])
    print('I chose ' + bot_choice)

    
    
    if player_input == 'rock':
        if bot_choice == 'rock':
            print('We tied.')
        elif bot_choice == 'paper':
            print('I won!')
        elif bot_choice == 'scissors':
            print('You won!')

    elif player_input == 'paper':
        if bot_choice == 'paper':
            print('We tied.')
        elif bot_choice == 'scissors':
            print('I won!')
        elif bot_choice == 'rock':
            print('You won!')

    elif player_input == 'scissors':
        if bot_choice == 'scissors':
            print('We tied.')
        elif bot_choice == 'rock':
            print('I won!')
        elif bot_choice == 'paper':
            print('You won!')
            
    
    else:
        print('Invalid choice: type rock, paper, or scissors!')

    
    player_input = input('Enter rock, paper, scissors, or quit ')



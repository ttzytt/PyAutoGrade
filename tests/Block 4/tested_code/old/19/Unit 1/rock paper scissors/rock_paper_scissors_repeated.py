


import random


player_choice = 0



while player_choice != -1:
    
    

    
    print(' ')
    
    random.seed()


    
    cheat_or_not = random.randint(1,10)

    
    player_choice = input("Enter rock, paper, scissors, or, quit (all lowercase): ")

    
    if cheat_or_not != 1:

        
        
        if player_choice == 'paper':
            player_choice = 1
            
        elif player_choice == 'rock':
            player_choice = 2
            
        elif player_choice == 'scissors':
            player_choice = 3
            
        elif player_choice == 'quit':
            
            player_choice = -1
            
        else:
            print("You did not follow the instructions")
            
            player_choice = 0

        
        computer_choice = random.randint(1,3)
        if computer_choice == player_choice:

            
            
            if player_choice == 1:
                print('I choose paper')
                print('We tie')
            elif player_choice == 2:
                print('I choose rock')
                print('We tie')
            else:
                print('I choose scissors')
                print('We tie')

        
        elif player_choice > computer_choice:
            
            if player_choice == 2:
                print('I choose paper')
                print('You lose')
            elif player_choice == 3 and computer_choice == 2:
                print('I choose rock')
                print('You lose')
            else:
                print('I choose paper')
                print('You win')

        
        elif player_choice < computer_choice and player_choice != 0 and player_choice != -1:
            
            if player_choice == 1 and computer_choice == 2:
                print('I choose rock')
                print('I lose')
            elif player_choice == 2:
                print('I choose scissors')
                print('You win')
            else:
                print('I choose scissors')
                print('You lose')

    
    elif cheat_or_not == 1:
        if player_choice == 'rock':
            print('I choose paper')
            print('I win, but I cheated')
            
        elif player_choice == 'paper':
            print('I choose scissors')
            print('I win, but I cheated')
            
        elif player_choice == 'scissors':
            print('I choose rock')
            print('I win, but I cheated')
            
        else:
            print("You didn't type rock, paper, or scissors")
    


print('Goodbye, play again next time')
    

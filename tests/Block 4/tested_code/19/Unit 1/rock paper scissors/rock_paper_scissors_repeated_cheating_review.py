


import random


p_choice = 0



while p_choice != -1:
    
    

    
    print(' ')
    
    random.seed()
    
    cheat_or_not = random.randint(1,10)

    p_choice = input("Enter rock, paper, scissors, or, quit (all lowercase): ")
    
    if cheat_or_not != 1:
        
        if p_choice == 'paper':
            p_choice = 1
        elif p_choice == 'rock':
            p_choice = 2
        elif p_choice == 'scissors':
            p_choice = 3
        elif p_choice == 'quit':
            p_choice = -1
        else:
            print("You did not follow the instructions")
            p_choice = 0
        

        c_choice = random.randint(1,3)

        if c_choice == p_choice:
            if p_choice == 1:
                print('I choose paper')
                print('We tie')
            elif p_choice == 2:
                print('I choose rock')
                print('We tie')
            else:
                print('I choose scissors')
                print('We tie')

        elif p_choice > c_choice:
            if p_choice == 2:
                print('I choose paper')
                print('You lose')
            elif p_choice == 3 and c_choice == 2:
                print('I choose rock')
                print('You lose')
            else:
                print('I choose paper')
                print('You win')

        elif p_choice < c_choice and p_choice != 0 and p_choice != -1:
            if p_choice == 1 and c_choice == 2:
                print('I choose rock')
                print('I lose')
            elif p_choice == 2:
                print('I choose scissors')
                print('You win')
            else:
                print('I choose scissors')
                print('You lose')

    elif cheat_or_not == 1:
        if p_choice == 'rock':
            print('I choose paper')
            print('I win, but I cheated')
        elif p_choice == 'paper':
            print('I choose scissors')
            print('I win, but I cheated')
        elif p_choice == 'scissors':
            print('I choose rock')
            print('I win, but I cheated')
        else:
            print("You didn't type rock, paper, or scissors")
    


print('Goodbye, play again next time')

    

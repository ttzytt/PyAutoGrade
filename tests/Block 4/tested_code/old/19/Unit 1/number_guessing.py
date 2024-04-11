


import random
random.seed()


computer_choice = random.randint(1,10)


player_choice = 0


while player_choice != computer_choice:
    
    player_choice = int(input('choose and integer between 1 and 10 (inclusive): '))

    if player_choice > computer_choice:
        print('too high')
    elif player_choice < computer_choice:
        print('too low')


print('Congrats u got it')
        

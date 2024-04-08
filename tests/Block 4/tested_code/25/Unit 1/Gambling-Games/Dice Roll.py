import random

random.seed()

play_again = 'yes'
cheating_prob = random.randint(5,15)
counter = 0

while play_again.lower() == 'yes':
    
    if play_again.lower() == 'yes':
        
        amount_bet = int(input('How much would you like to bet?: '))
        player_num = int(input('Choose an integer between 1 and 6: '))
        dice = random.randint(1,6)
    
    if player_num < 1 or player_num > 6:
        print('READ THE INSTRUCTIONS!')
        
    elif dice == player_num and counter >= cheating_prob:
        print('You won ' + str(4 * amount_bet) + '.')
        print('Now leave and never come back.')
        play_again = 'no'
        
    else:
        print('Your number was incorrect.')
        print('You lost ' + str(amount_bet) + '.')
        play_again = input('Would you like to play again?: ')

    print()

    counter = counter + 1
    
if play_again.lower() == 'no':
    print('Sorry to see you go.')

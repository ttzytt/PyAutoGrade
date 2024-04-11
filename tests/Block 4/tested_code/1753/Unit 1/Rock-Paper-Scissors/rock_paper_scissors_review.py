

computer = random.choice(['Rock', 'Paper', 'Scissors'])
player = input('Choose rock, paper, or scissors: ')


if computer == 'Rock':
    print('I choose rock.')
    
    if player.lower() == 'rock':
        print('We tied.')
    elif player.lower() == 'Paper':
        print('You win!')
    elif player.lower() == 'Scissors':
        print('You lose!')
    else:
        print('Try again.')


elif computer == 'Paper':
    print('I choose paper.')
    if player.lower() == 'Rock':
        print('You lose!')
    elif player.lower() == 'Paper':
        print('We tied.')
    elif player.lower() == 'Scissors':
        print('You win!')
    else:
        print('Try again.')


else:  
    print('I choose scissors.')
    if player.lower() == 'Rock':
        print('You win!')
    elif player.lower() == 'Paper':
        print('You lose!')
    elif player.lower() == 'Scissors':
        print('We tied.')
    else:
        print('Try again.')




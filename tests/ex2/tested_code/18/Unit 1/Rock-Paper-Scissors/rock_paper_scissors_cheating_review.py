



player = input('Choose rock, paper, or scissors: ')


if player.lower() == 'rock':
    print('I choose paper.')
    print('You lose!')


elif player.lower() == 'paper':
        print('I choose scissors.')
        print('You lose!')


elif player.lower() == 'scissors':
    print('I choose rock.')
    print('You lose!')


else:
    print('Try again.')



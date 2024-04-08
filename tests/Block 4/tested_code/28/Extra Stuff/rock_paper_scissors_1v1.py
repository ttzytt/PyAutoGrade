



user1_choice = input("Player 1, enter 'rock' or 'paper' or 'scissors': ").lower()

user2_choice = input("Player 2, enter 'rock' or 'paper' or 'scissors': ").lower()





if user1_choice == 'paper':
    if user2_choice == 'rock':
        print('Player 1 wins.')
    elif user2_choice == 'scissors':
        print('Player 2 wins.')
    else:
        print('You tie.')
        

elif user1_choice == 'rock':
    if user2_choice == 'scissors':
        print('Player 1 wins.')
    elif user2_choice == 'paper':
        print('Player 2 wins.')
    else:
        print('You tie.')


else:
    if user2_choice == 'paper':
        print('Player 1 wins.')
    elif user2_choice == 'rock':
        print('Player 2 wins.')
    else:
        print('You tie.')

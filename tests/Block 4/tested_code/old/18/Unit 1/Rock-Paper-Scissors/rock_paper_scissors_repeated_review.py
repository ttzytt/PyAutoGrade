





import random

while True:   
    player = input("Enter 'rock', 'paper', 'scissors', or 'quit' to end the game: ")

    if player == 'quit':   
        print("Thanks for playing! Goodbye.")
        break

    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"I chose {computer}.")

    if player == computer:
        print('We tie.')
    elif player == 'rock' and computer == 'paper':
        print('I win')
    elif player == 'scissors' and computer == 'rock':
        print('I win')
    elif player == 'paper' and computer == 'scissors':
        print('I win')
    elif player == 'paper' and computer == 'rock':
        print('You win')
    elif player == 'rock' and computer == 'scissors':
        print('You win')
    elif player == 'scissors' and computer == 'paper':
        print('You win')
    else:
        print(player + ' is not one of the options. Please choose rock, paper, scissors, or quit.')

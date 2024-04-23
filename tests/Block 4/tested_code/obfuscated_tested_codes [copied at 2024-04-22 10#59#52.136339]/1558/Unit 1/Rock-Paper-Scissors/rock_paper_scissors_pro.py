


"""
This program lets the user play rock paper scissors with
the computer repeatedly until they quit, and after each round
the computer prints the score
"""
import random


def rps_score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0  

    if (choice_1 == 'rock' and choice_2 == 'scissors') or \
       (choice_1 == 'scissors' and choice_2 == 'paper') or \
       (choice_1 == 'paper' and choice_2 == 'rock'):
        return 1  
    else:
        return -1  


player_score = 0
computer_score = 0


player_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()


while player_choice == 'rock'or player_choice == 'paper' or player_choice == 'scissors':
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    print(f'I chose {computer_choice}.')
    
    result = rps_score_round(player_choice, computer_choice)

    if result == 0:
        print(f'We tie.')
        print(f'Score: Player {player_score} - Computer {computer_score}')
        print()
    elif result == 1:
        player_score = player_score + 1
        print(f'You win.')
        print(f'Score: Player {player_score} - Computer {computer_score}')
        print()
    else:
        computer_score = computer_score + 1
        print(f'I win.')
        print(f'Score: Player {player_score} - Computer {computer_score}')
        print()

    player_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()


while player_choice != 'q':
    print('Invalid input. Please enter one of the four choices.')
    print()
    player_choice = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()


print('Thank you for playing!')    
print(f'Final Score: Player {player_score} - Computer {computer_score}')



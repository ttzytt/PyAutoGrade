import random


def rps_score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0
    if (choice_1 == 'rock' and choice_2 == 'scissors') or 
       (choice_1 == 'scissors' and choice_2 == 'paper') or 
       (choice_1 == 'paper' and choice_2 == 'rock'):
        return 1
    return -1

user_score = 0

while True:
    user_input = input("Enter 'rock', 'paper', or 'scissors', or 'q' to quit: ")

    if user_input == 'q':
        print("Thanks for playing! Your total score is:", user_score)
        break

    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please try again.")
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chose:", computer_choice)

    round_score = rps_score_round(user_input, computer_choice)
    if round_score == 0:
        print("It's a tie!")
    elif round_score == 1:
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        user_score -= 1

    print("Current score:", user_score)

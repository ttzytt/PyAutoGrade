



import random
random.seed()


def score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0
    elif (
        (choice_1 == 'rock' and choice_2 == 'scissors') or
        (choice_1 == 'paper' and choice_2 == 'rock') or
        (choice_1 == 'scissors' and choice_2 == 'paper')
    ):
        return 1
    else:
        return -1


def user():
    while True:
        player_input = input("Enter 'rock', 'paper', or 'scissors', or 'quit': ")
        if player_input in ['rock', 'paper', 'scissors', 'quit']:
            return player_input
        else:
            print("Invalid input; enter 'rock', 'paper', 'scissors', or 'quit'.")

score = int(0)

while True:
    choice = user()
    
    
    if choice == 'quit':
        break

    bot_choice = random.choice(['rock', 'paper', 'scissors'])  

    result = score_round(choice, bot_choice)

    print('You chose ' + choice + ', and I chose ' + bot_choice)

    
    if result == 1:
        print('You won!')
        score += 1
    elif result == -1:
        print('You lost.')
        score -= 1
    else:
        print('We tied!')

    print('Your current score is ' + str(score))

print('Thanks for playing!')

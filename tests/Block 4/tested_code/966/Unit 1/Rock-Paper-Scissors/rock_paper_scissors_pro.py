


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
        user_input = input('enter rock, paper, scissors, or quit to quit: ')
        if user_input in ['rock', 'paper', 'scissors', 'quit']:
            return user_input
        else:
            print("invalid input try again")

score = int(0)

while True:
    choice = user()

    
    if choice == 'quit':
        break

    computer_choice = random.choice(['rock','paper','scissors']) 

    result = score_round(choice, computer_choice)

    print('you choose ' + choice + ' ' + 'computer choose ' + computer_choice)

    
    
    if result == 1:
        print('you win this round')
        score += 1
    elif result == -1:
        print('you lose this round')
        score -= 1
    else:
        print('its a tie')

    
    print('your current score is ' + str(score))

print('thanks for playing')





import random

random.seed()


def rps_score_round(choice_1, choice_2):
    if choice_1 == 'rock':
        if choice_2 == 'paper':
            return -1
        if choice_2 == 'scissor':
            return 1

    elif choice_1 == 'paper':
        if choice_2 == 'rock':
            return 1
        elif choice_2 == 'scissor':
            return -1

    elif choice_1 == 'scissor':
        if choice_2 == 'rock':
           return -1
        elif choice_2 == 'paper':
            return 1

    if choice_1 == choice_2:
        return 0


point = 0
response = 'yes'

while response == 'yes':
    choice_1 = input('Enter rock, paper , scissor, or q to quit: ')
    choice_2 = random.choice(['rock' , 'paper' , 'scissor'])
    
    while choice_1 != 'rock' and choice_1 != 'paper' and choice_1 != 'scissor' and choice_1 != 'q':
        print('Previous input not valid, follow instructions')
        choice_1 = input('Enter rock, paper, scissor, or q to quit: ')
    
    if choice_1 == 'q':
        response = 'no'
        print('Sad to see you go')
    elif rps_score_round(choice_1, choice_2) == 0:
        print('I choose ' + choice_2 + '.')
        print('We Tie')
    elif rps_score_round(choice_1, choice_2) == -1:
        print('I choose ' + choice_2 + '.')
        print('I win')
        point -= 1
    elif rps_score_round(choice_1, choice_2) == 1:
        print('I choose ' + choice_2 + '.')
        print('You Win')
        point += 1

    
    print('You have ' + str(point) + ' point(s).')
    
              





import random 

random.seed()

playerguess = int(input('The computer has thought of a number from 1 to 10. Guess what it is.'))
computernum = random.choice([1,2,3,4,5,6,7,8,9,10])

while playerguess > computernum or playerguess < computernum:


    if playerguess > computernum:
        print('Too high!')
    elif playerguess < computernum:
        print('Too low!')
    playerguess = int(input('Guess again!'))
else:
    print('You guessed correctly!')





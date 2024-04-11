


import random

number = random.randint(1,10)
again = True
while again:
    user = int(input('guess a number between 1 and 10: '))

    if user == number:
        print('you got it right')
        again = False
    elif user < number:
        print('too low')
    elif user > number:
        print('too high')



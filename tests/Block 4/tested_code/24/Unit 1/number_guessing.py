


import random

random.seed()

print("Let's play a number game.")


response = str('yes')

while response == 'yes':
    
    random_number = str(random.randint(1, 10))
    player = str(input("I have chosen a number between 1 and 10 (exclusive). Try to guess it!" ))

    while player != random_number:
        if player > random_number:
            print("That number is too high!")
        elif player < random_number:
            print("That number is too low.")
        player = input("Guess again!")
    else:
        print("Nice guess! Thats right!")
    
    response = input("Do you want to play again? ('yes' or 'no') ")
else:
    print("I'm sad to see you leave, come play another time!")












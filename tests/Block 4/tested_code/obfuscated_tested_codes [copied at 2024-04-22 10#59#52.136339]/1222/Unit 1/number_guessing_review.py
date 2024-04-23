


import random

random.seed()

random_number = random.randint(1, 10)

print("Let's play a number game.")
print("I will choose a number between 1 and 10")
print("Try to guess it! ")



player = int(input('What is your guess?'))


while player != str(random_number):
    
    
    if str(player) > str(random_number):
        print("That number is too high!")
    elif str(player) < str(random_number):
        print("That number is too low.")
    
    player = input("Guess again!")

else:
    print("Nice guess! Thats right!")


response = input("Do you want to play again? ('yes' or 'no') ")







while response == 'yes':
    
    random_number = random.randint(1, 10)
    player = int(input("I have chosen a number between 1 and 10. Try to guess it!" ))

    
    while player != str(random_number):
        if str(player) > str(random_number):
            print("That number is too high!")
        elif str(player) < str(random_number):
            print("That number is too low.")
        player = input("Guess again!")
    else:
        print("Nice guess! Thats right!")
    response = input("Do you want to play again? ('yes' or 'no') ")
else:
    print("I'm sad to see you leave, come play another time!")












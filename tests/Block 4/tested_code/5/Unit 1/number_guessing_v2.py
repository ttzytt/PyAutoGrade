


import random

random.seed()

print("Let's play a number game.")


response = str('yes')
want_hint = str('yes')


while response == 'yes':
    
    
    random_number = str(random.randint(1, 10))
    player = str(input("I have chosen a number between 1 and 10 (exclusive). Try to guess it! "))
    
    while player != random_number: 
        if player > random_number:
            print("That number is too high!")
        elif player < random_number:
            print("That number is too low.")
        want_hint = input("Do you want a hint?(yes or no) ")
        
        if want_hint == 'yes':
            if random_number == '5':
                print("The number is greater than or equal to 5")
            elif random_number < '5':
                print("The number is less than 5")
            elif random_number > '5':
                print("The number is greater than 5")

        player = input("Guess again! ")
        
    print("Nice guess! Thats right!")
        
    
    response = input("Do you want to play again? ('yes' or 'no') ")
    
else:
    print("I'm sad to see you leave, come play another time!")

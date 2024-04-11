


import random

random.seed()


print("Hello, lets play a game of rock paper scissors.")


response = 'yes'

while response == 'yes':
    
    
    random.seed()

    player = input("Choose one: rock, paper, or scissors? (all lowercase, no spaces) ")

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("I choose " + computer_choice + ".")

    
    if computer_choice == player:
        print("Looks like we tied.")

    elif computer_choice == ('rock'):
        if player == ('paper'):
            print("Looks like I lost, Good Game!")
        elif player == ('scissors'):
            print("I win gg ez.")

    elif computer_choice == ('paper'):
        if player == ('rock'):
            print("I win gg ez.")
        elif player == ('scissors'):
            print("Looks like I lost, Good Game!")

    elif computer_choice == ('scissors'):
        if player == ('rock'):
           print("Looks like I lost, Good Game!")
        elif player == ('paper'):
            print("I win gg ez.")
    response = input("Do you want to play again? ( Type 'yes' or 'no') ")
    

print("I'm sad to see you go :(")
 




import random




print("Hello, lets play a game of rock paper scissors.")

player = input("Choose one: rock, paper, or scissors? (all lowercase, no spaces) ")


computer = random.choice(['rock', 'paper', 'scissors'])

print("I choose " + computer + ".")



if computer == player:
    
    print("Looks like we tied.")


if computer == ('rock'):
    if player == ('paper'):
        print("Looks like I lost, Good Game!")
    elif player == ('scissors'):
        print("I win gg ez.")

elif computer == ('paper'):
    if player == ('rock'):
        print("I win gg ez.")
    elif player == ('scissors'):
        print("Looks like I lost, Good Game!")

elif computer == ('scissors'):
    if player == ('rock'):
       print("Looks like I lost, Good Game!")
    elif player == ('paper'):
        print("I win gg ez.")

response = input("Do you want to play again? ( Type 'yes' or 'no' ) ")



while response == 'yes':

    
    
    print("Ok, lets play!")

    player = input("Choose one: rock, paper, or scissors? (all lowercase, no spaces) ")

    computer = random.choice(['rock', 'paper', 'scissors'])

    print("I choose " + computer + ".")

    if computer == player:
        print("Looks like we tied.")

    elif computer == ('rock'):
        if player == ('paper'):
            print("Looks like I lost, Good Game!")
        elif player == ('scissors'):
            print("I win gg ez.")

    elif computer == ('paper'):
        if player == ('rock'):
            print("I win gg ez.")
        elif player == ('scissors'):
            print("Looks like I lost, Good Game!")

    elif computer == ('scissors'):
        if player == ('rock'):
           print("Looks like I lost, Good Game!")
        elif player == ('paper'):
            print("I win gg ez.")
    response = input("Do you want to play again? ( Type 'yes' or 'no') ")
    

print("I'm sad to see you go :(")
 

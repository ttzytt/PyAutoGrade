




user = input("Enter 'rock' 'paper' or 'scissors' : ")


import random
random.seed()
computer_select_list = ['rock', 'paper', 'scissors']

computer_select = random.choice(computer_select_list)


print("I choose " + computer_select)

if user == computer_select:
    print("We tie.")


if user == "rock":
    if computer_select == "paper":
        print("I win.")
    elif computer_select == "scissors":
        print("You win.")

elif user == "paper":
    if computer_select == "rock":
        print("You win.")
    elif computer_select == "scissors":
        print("I win.")

elif user == "scissors":
    if computer_select == "rock":
        print("You win.")
    elif computer_select == "paper":
        print("I win.")

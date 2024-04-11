





user = input("Enter 'rock' or 'paper': ")


import random

computer_select_list = ['rock', 'paper']
computer_select = random.choice(computer_select_list)


print("I choose " + computer_select)


if (user == "rock"):
    if(computer_select == "rock"):
        print("We tie.")
    if(computer_select == "paper"):
        print("I win.")

if (user == "paper"):
    if(computer_select == "rock"):
        print("You win.")
    if(computer_select == "paper"):
        print("We tie.")



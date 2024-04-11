



import random

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
user_action = input("Enter a choice (rock, paper, scissors): ")

print("I choose " +computer_action + ".")

if computer_action == user_action:
    print("It's a tie.")
elif user_action == "paper":
    if computer_action == "rock":
        print("You won!")
    elif computer_action == "scissors":
        print("You lost!")
elif user_action == "rock":
    if computer_action == "paper":
        print("You lost!")
    elif computer_action == "scissors":
        print("You won!")
elif user_action == "scissors":
    if computer_action == "paper":
        print("You won!")
    elif computer_action == "rock":
        print("You lost!")

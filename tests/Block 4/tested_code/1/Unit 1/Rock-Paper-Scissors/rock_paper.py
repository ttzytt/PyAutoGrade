



import random

possible_actions = ["rock", "paper"]
computer_action = random.choice(possible_actions)
user_action = input("Enter a choice, rock or paper? ")

print("I choose " +computer_action + ".")

if computer_action == user_action:
    print("It's a tie.")
elif user_action == "paper" and computer_action == "rock":
    print("You won!")
elif user_action == "rock" and computer_action == "paper":
    print("You lost!")



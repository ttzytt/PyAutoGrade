






from random import choice


user_choice = input("Rock or Paper: ").lower()

computer_choice = choice(["rock","paper"])

print("I choose %s." % computer_choice)

if user_choice == "rock":
    if computer_choice == "rock":
        print("We tie.")
    if computer_choice == "paper":
        print("I win.")
if user_choice == "paper":
    if computer_choice == "rock":
        print("You win.")
    if computer_choice == "paper":
        print("We tie.")

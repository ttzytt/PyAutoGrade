



print("Hi! This is a rock n paper GAMBLING game! You have 100$ to start with.")




import random

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
user_fund = 100


while user_fund > 0 :
    user_bet = int(input("How much money would you like to bet in this round? "))
    while not int(user_bet) in range(1, int(user_fund) + 1): 
        user_bet = input("You can't bet more money than you have. Plz re-enter your bet: ")
    user_action = input("Enter a choice (rock, paper, scissors): ")
    print("I choose " +computer_action + ".")

    if computer_action == user_action:
        print("It's a tie. Phew!")
    elif user_action == "paper" and computer_action == "rock":
        print("You won " + "$" + str(user_bet) + "!")
        user_fund = user_fund + user_bet
    elif user_action == "paper" and computer_action == "scissors":
        print("You lost " + "$" + str(user_bet) + ".")
        user_fund = user_fund - user_bet
    elif user_action == "rock" and computer_action == "paper":
        print("You lost " + "$" + str(user_bet) + ".")
        user_fund = user_fund - user_bet
    elif user_action == "rock" and computer_action == "scissors":
        print("You won " + "$" + str(user_bet) + "!")
        user_fund = user_fund + user_bet
    elif user_action == "scissors" and computer_action == "paper":
        print("You won " + "$" + str(user_bet) + "!")
        user_fund = user_fund + user_bet
    elif user_action == "scissors" and computer_action == "rock":
        print("You lost " + "$" + str(user_bet) + ".")
        user_fund = user_fund - user_bet
    print("Now you have $" + str(user_fund) + " in total.")

    '''if user_fund > 0: # to stop the while loop if the use decide to quit
        user_quit = input("Do you still want to play(yes or no)? ")
        if user_quit == 'no':
            print("It was a fun game. Good luck next time!")
        break'''

else:
    print("It was a fun game. Good luck next time!")



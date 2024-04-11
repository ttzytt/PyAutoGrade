





user_choice = input("Rock, Paper, or Scissors: ").lower()

winning_battles = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }


computer_choice = winning_battles.get(user_choice, "nothing since you're cheating.")

print("I choose %s." % computer_choice)
print("I win.")


'''
if user_choice == "rock":

    # dictionary used
    rock_battles = {
        "rock": "We tie.",
        "paper": "I win.",
        "scissors": "You win."
    }

    print(rock_battles.get(computer_choice))
    
if user_choice == "paper":
    
    paper_battles = {
        "rock": "You win.",
        "paper": "We tie.",
        "scissors": "I win."
    }

    print(paper_battles.get(computer_choice))
    
if user_choice == "scissors":
    
    scissors_battles = {
        "rock": "I win.",
        "paper": "You win.",
        "scissors": "We tie."
    }

    print(scissors_battles.get(computer_choice))
'''

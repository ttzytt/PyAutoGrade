





user_choice = input("Rock, Paper, or Scissors: ").lower()

winning_battles = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }


computer_choice = winning_battles.get(user_choice, "nothing since you're cheating.")

print("I choose %s." % computer_choice)
print("I win.")







import random

def cheat_move(player_move):

    if player_move == "rock":
        return "paper"
    if player_move == "paper":
        return "scissors"
    if player_move == "scissors":
        return "rock"

print("Welcome to Rock, Paper, Scissors!")
print("Enter 'rock', 'paper', 'scissors' to play.")
print("Enter 'quit' anytime to stop playing.")



while True:
    player_move = input("Make your move: ")
    
    if player_move == 'quit':
        print("Thanks for playing! Goodbye.")
        break

    if player_move not in ('rock', 'paper', 'scissors'):
        print("Invalid choice. Please pick 'rock', 'paper', 'scissors' or type 'quit' to exit.")
        continue

    
    if random.random() < 0.10:
        computer_move = cheat_move(player_move)
    else:
        computer_move = random.choice(['rock', 'paper', 'scissors'])
    
    print("Computer selected:", computer_move)

    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'scissors' and computer_move == 'paper') or \
         (player_move == 'paper' and computer_move == 'rock'):
        print("You win!")
    else:
        print("Computer wins!")

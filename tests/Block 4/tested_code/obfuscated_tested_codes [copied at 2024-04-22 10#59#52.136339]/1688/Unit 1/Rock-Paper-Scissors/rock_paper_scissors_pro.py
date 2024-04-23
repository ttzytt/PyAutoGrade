


import random
random.seed()


def rps_score_round(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0
    if (choice_1 == 'rock' and choice_2 == 'scissors') or \
       (choice_1 == 'scissors' and choice_2 == 'paper') or \
       (choice_1 == 'paper' and choice_2 == 'rock'):
        return 1
    return -1

score = 0


while True:
    user_choice = input("\nEnter 'rock', 'paper', or 'scissors', or 'q' to quit: ").lower()
    
    
    if user_choice not in ['rock', 'paper', 'scissors', 'q']:
        print("Invalid input. Try again.")
        continue
    
    
    if user_choice == 'q':
        break
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}\n")
    
    
    round_score = rps_score_round(user_choice, computer_choice)
    score += round_score

    if round_score == 1:
        print("🎉Congrats! You win!")
    elif round_score == 0:
        print("🤝We tie.")
    else:
        print("😢Sorry, you lose.")
        
    
    print("\n--------------------------------------------------\n")
    print(f"Total Score: {score}")
    
    


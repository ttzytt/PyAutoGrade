


import random
random.seed()

while True:   
    
    user_choice = input("Enter 'rock', 'paper', 'scissors' or 'quit' to stop: ").lower()
    if user_choice == 'quit':
        break   

    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Try again.")
        continue

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    
    print("I choose " + computer_choice + ".")


    
    if user_choice == computer_choice:
        print("We Tie.")
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You Win.")
    
    else:
        print("I win!")










































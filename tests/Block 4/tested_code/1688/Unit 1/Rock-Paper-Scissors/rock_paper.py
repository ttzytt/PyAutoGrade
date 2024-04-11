




import random
random.seed()


user_choice = input("Enter 'rock' or 'paper': ")


computer_choice = random.choice(['rock', 'paper'])



print(f"I choose {computer_choice}.")



if user_choice == computer_choice:
    
    print("We tie.")
    
else:
    
    print("You win." if user_choice == 'paper' else "I win.")













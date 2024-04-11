



import random
random.seed()



user_choice = input("Enter 'rock', 'paper', or 'scissors': ")


computer_choice = random.choice(['rock', 'paper', 'scissors'])



print(f"I choose {computer_choice}.")



if user_choice == computer_choice:
    
    print("We tie.")
    
elif computer_choice == 'rock':
    
    print("You win." if user_choice == 'paper' else "I win.")
    
elif computer_choice == 'paper':
    
    print("You win." if user_choice == 'scissors' else "I win.")

elif computer_choice == 'scissors':
    
    print("You win." if user_choice == 'rock' else "I win.")

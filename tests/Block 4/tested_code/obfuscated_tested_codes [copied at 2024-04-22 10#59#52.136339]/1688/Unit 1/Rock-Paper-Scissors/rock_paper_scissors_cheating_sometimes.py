



import random
random.seed()



user_choice = input("Enter 'rock', 'paper', or 'scissors': ")




computer_choice = random.choice(['rock', 'paper', 'scissors'])



if random.random() < 0.1:
    
    cheat_map = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    computer_choice = cheat_map[user_choice]



win_cases = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]



if (user_choice, computer_choice) in win_cases:
    
    result = "You win."
    
elif user_choice != computer_choice:
    
    result = "I win."
    
else:
    result = "We tie."



print(f"I choose {computer_choice}. \n{result}")








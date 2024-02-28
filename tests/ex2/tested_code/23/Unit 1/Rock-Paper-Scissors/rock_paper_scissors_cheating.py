



user_choice = input("Enter 'rock', 'paper', or 'scissors': ")



if user_choice == 'rock':
    
    computer_choice = 'paper'
    
elif user_choice == 'paper':
    
    computer_choice = 'scissors'

else:
     
    computer_choice = 'rock'



print(f"I choose {computer_choice}. \nAHA! I WIN!")

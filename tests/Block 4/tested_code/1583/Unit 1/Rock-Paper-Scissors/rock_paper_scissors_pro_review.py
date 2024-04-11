




import random








def rps_score_round(choice_1, choice_2):
    
    if choice_1 == 'paper':
        
        if choice_2 == 'rock':
            return 1
        elif choice_2 == 'scissors':
            return -1
        else:
            return 0
            
    elif choice_1 == 'rock':
        if choice_2 == 'scissors':
            return 1
        elif choice_2 == 'paper':
            return -1
        else:
            return 0

    elif choice_1 == 'scissors':
        if choice_2 == 'paper':
            return 1
        elif choice_2 == 'rock':
            return -1
        else:
            return 0
    else:
        return None



user_score = 0
computer_score = 0


user_choice = input("Enter 'rock' or 'paper' or 'scissors', or " +
                    "'quit' if you want to quit: ").lower()

while user_choice != 'quit': 
    
    random_choice = random.randint(0, 2)
    if random_choice == 0:
        computer_choice = 'rock'
    elif random_choice == 1:
        computer_choice = 'paper'
    else:
        computer_choice = 'scissors'

    
    if rps_score_round(user_choice, computer_choice) is None:
        print('Invalid input, try again.')
    else: 
        print('I choose ' + computer_choice + '.')
        
        if rps_score_round(user_choice, computer_choice) == 1: 
            print('You win.')
            user_score = user_score + 1
        elif rps_score_round(user_choice, computer_choice) == -1: 
            print('I win.')
            computer_score = computer_score + 1
        elif rps_score_round(user_choice, computer_choice) == 0: 
            print('We tie.')
            

        print('Player score: ' + str(user_score))
        print('Computer score: ' + str(computer_score))
    

    
    
    print()
    user_choice = input("Enter 'rock' or 'paper' or 'scissors', or " +
                        "'quit' if you want to quit: ").lower()



print()
print('Final score:')
print('Player: ' + str(user_score) + ', Computer: ' + str(computer_score))

if user_score > computer_score:
    print('You win, dang it!')
elif user_score < computer_score:
    print('I win, you suck.')
else:
    print('We tie, we should run it back sometime.')

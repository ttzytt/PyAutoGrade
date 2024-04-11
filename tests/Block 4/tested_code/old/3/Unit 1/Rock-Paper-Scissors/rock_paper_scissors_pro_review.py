







import random
random.seed()


choice = input("Enter 'rock', 'paper', 'scissors' or 'q' to quit: ")
choice2 = random.choice(['rock', 'paper', 'scissors'])
score = 0
def rps_score_round(choice, choice2):
    if choice == choice2:
        return 0
    elif ((choice == 'rock' and choice2 == 'paper')
              or (choice == 'paper' and choice2 == 'scissor')
              or (choice == 'scissor' and choice2 == 'rock')):
        return -1
    else:
        return +1


while choice != "q":

    
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("I choose " + computer_choice)
 
    
    if ((choice == 'rock' and computer_choice == 'paper')
            or (choice == 'paper' and computer_choice == 'scissors')
            or (choice == 'scissors' and computer_choice == 'rock')):
        print('I win.')
        score = score -1
        print('You score is ' + str(score))
    
    elif ((choice == 'paper' and computer_choice == 'rock')
            or (choice == 'scissors'and computer_choice == 'paper')
            or (choice == 'rock' and computer_choice == 'scissors')):
        print('You win.')
        score = score + 1
        print('You score is ' + str(score))
    elif choice != ('rock' or 'paper' or 'scissors' or 'q'):
        print('Try again!')

    else:
        print('We tie.')
        print('You score is ' + str(score))
    choice = input("Enter 'rock', 'paper', 'scissors' or 'q': ")
print('Bye.')

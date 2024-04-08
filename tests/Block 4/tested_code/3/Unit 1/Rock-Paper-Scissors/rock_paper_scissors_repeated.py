




import random
random.seed()
choice = input("Enter 'rock', 'paper', 'scissors' or 'quit': ")


while choice != "quit":



    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print("I choose " + computer_choice)


    if ((choice == 'rock' and computer_choice == 'paper')
            or (choice == 'paper' and computer_choice == 'scissors')
            or (choice == 'scissors' and computer_choice == 'rock')):
        print('I win.')
    
    elif ((choice == 'paper' and computer_choice == 'rock')
            or (choice == 'scissors'and computer_choice == 'paper')
            or (choice == 'rock' and computer_choice == 'scissors')):
        print('You win.')
    
    else:
        print('We tie.')
    choice = input("Enter 'rock', 'paper', 'scissors' or 'quit': ")
print('Bye.')

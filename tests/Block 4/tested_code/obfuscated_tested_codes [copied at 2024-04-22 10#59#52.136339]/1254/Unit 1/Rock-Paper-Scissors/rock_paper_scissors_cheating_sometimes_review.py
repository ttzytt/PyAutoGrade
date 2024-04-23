


import random

random.seed()

player = input("Enter 'rock', 'paper' or 'scissors': ")

random_number = random.randint(1,10)





if random_number == 1:
    if player == 'rock':
        computer = 'paper.'
        print("I choose " + computer)
        print ('I win.')
    

    elif player == 'paper':
        computer = 'scissors.'
        print("I choose " + computer)
        print ('I win.')

    elif player == 'scissors':
        computer = 'rock.'
        print("I choose " + computer)
        print ('I win.')


else:
    computer = random.choice(('rock', 'paper', 'scissors'))
    print ("I choose " + computer + ".")
    
    if player == computer:
        print('We tie.')


    elif player == 'rock':
        if computer == 'paper':
            print('I win.')
        elif computer == 'scissors':
            print('You win.')

    elif player == 'paper':
        if computer =='rock':
            print('You win.')
        elif computer == 'scissors':
            print('I win.')

    elif player == 'scissors':
        if computer == 'rock':
            print ('I win.')
        elif computer == 'paper':
            print('You win.')

'''R
No explanation
no spacing
This code is good
'''

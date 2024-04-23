


import random

random.seed()


choice = str(input("Enter 'rock', 'paper' or 'scissors': "))


choice2 = random.choice(['rock', 'paper', 'scissors'])
print("I choose " + choice2)


if (choice == 'rock' and choice2 == 'paper')
        or (choice == 'paper' and choice2 == 'scissors')
        or (choice == 'scissors' and choice2 == 'rock'):
    print('I win.')
    
elif (choice == 'paper' and choice2 == 'rock')
        or (choice == 'scissors'and choice2 == 'paper')
        or (choice == 'rock' and choice2 == 'scissors'):
    print('You win.')
    
else:
    print('We tie.')

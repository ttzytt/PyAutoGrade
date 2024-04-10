



import random

random.seed()


print("This is rock paper scissors, type 'quit' to stop playing.")


user = input("Choose 'rock', 'paper', 'scissors' or 'quit': ")
while user != 'quit':
    computer = random.choice(['rock', 'paper', 'scissors'])
    print("I choose", computer)

    if user == computer:
        print('We tie.')

    elif (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper') or (user == 'rock' and computer == 'scissors'):
        print('You won.')

    else:
        print('I win.')

    user = input("Choose 'rock', 'paper', 'scissors' or 'quit': ")


print('Unfortunate you must go...')
print('Hope you come back later!')

      


    

        
    

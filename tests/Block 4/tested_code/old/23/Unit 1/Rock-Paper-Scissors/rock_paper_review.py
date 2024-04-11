





import random 

random.seed()

user = input("Enter 'rock' or 'paper': ") 

comp = random.choice(['rock', 'paper']) 

print('I choose ' + comp + '.')

if user == 'rock':   

    if comp == 'rock':
        print('We tie.')
    else:
        print('I win.')

else:

    if comp == 'rock':
        print('You win.')
    else:
        print('We tie.')


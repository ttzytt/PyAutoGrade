


import random

random.seed()


choice = str(input("Enter 'rock' or 'paper': "))


choice2 = random.choice(['rock', 'paper'])
print("I choose " + choice2)


if choice == 'rock' and choice2 == 'paper':
    print('I win.')
elif choice == 'paper' and choice2 == 'rock':
    print('You win.')
else:
    print('We tie.')

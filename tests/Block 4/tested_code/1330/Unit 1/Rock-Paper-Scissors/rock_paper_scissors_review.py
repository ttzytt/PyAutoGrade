




import random

random.seed()


choice = str(input("Enter 'rock', 'paper' or 'scissor': "))


choice2 = random.choice(['rock', 'paper', 'scissor'])
print("I choose " + choice2)


if (choice == 'rock' and choice2 == 'paper') or (choice == 'paper' and choice2 == 'scissor') or (choice == 'scissor' and choice2 == 'rock'):
    print('I win.')
elif (choice == 'paper' and choice2 == 'rock') or (choice == 'scissor' and choice2 == 'papper') or (choice == 'rock' and choice2 == 'scissor'):
    print('You win.')
    
else:
    print('We tie.')

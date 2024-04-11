



import random

random.seed() 

user = input("Enter 'rock' or 'paper': ") 

computer = random.choice(['rock', 'paper', 'scissors']) 

print('I choose ' + computer + '.') 

if user == computer: 
    print('We tie.')


elif user == 'rock' and computer == 'paper':
    print('I win.')
elif user == 'rock' and computer == 'scissors':
    print('You win.')

elif user == 'paper' and computer == 'rock':
    print('You win.')
elif user == 'paper' and computer == 'scissors':
    print('I win.')

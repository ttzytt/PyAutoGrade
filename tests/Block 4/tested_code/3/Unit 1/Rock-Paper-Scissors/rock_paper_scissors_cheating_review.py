




import random 

random.seed()

user = input("Enter 'rock' or 'paper' or 'scissors': ") 

if user == 'rock': 
    comp = 'paper'

elif user == 'paper':
    comp = 'scissors'
        
else:
    comp = 'rock'

print('I choose '+comp+'.')
print('I win.')

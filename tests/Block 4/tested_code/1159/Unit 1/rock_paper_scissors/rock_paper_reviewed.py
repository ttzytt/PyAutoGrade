




import random

random.seed()

user = input('Enter rock or paper')
auto = random.choice(['rock','paper'])
print('I choose '+ auto) 
if user == 'rock':
 if auto == 'rock':
  print('We tie')
 elif auto == 'paper':
  print('I win, haha!')
if user == 'paper':
 if auto == 'rock':
  print('You win, congrats!')
 elif auto == 'paper':
  print('We tie')

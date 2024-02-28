



import random

random.seed()

user = input('Enter rock or paper: ')
auto = random.choice(['rock','paper'])


if user == 'rock' or user == 'paper':
 print('I choose ' + auto)
 if user == 'rock':
  if auto == 'rock':
   print('We tie')
  elif auto == 'paper':
   print('I win, haha!')
 elif user == 'paper':
  if auto == 'rock':
   print('You win, congrats!')
  elif auto == 'paper':
   print('We tie')
elif user == 'scissors':
 print('Sorry, scissors isn\'t included in this game')
else:
 print('You should only input rock or paper')

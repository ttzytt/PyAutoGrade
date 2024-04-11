


import random

random.seed()

print('If you wish to exit the game, input quit')


user = input('Please input rock, paper, scissors or quit: ')
auto = random.choice(['rock','paper','scissors'])


while user == 'rock' or user == 'paper' or user == 'scissors':
 print('I choose '+ auto)
 if user == 'paper':
  if auto == 'scissors':
   print('I win, haha!')
  elif auto == 'rock':
   print('You win, congrats!')
  elif auto == 'paper':
   print('We tie')
 elif user == 'rock':
  if auto == 'paper':
   print('I win, haha!')
  elif auto == 'scissors':
   print('You win, congrats')
  elif auto == 'rock':
   print('We tie')
 elif user == 'scissors':
  if auto == 'rock':
   print('I win, haha!')
  elif auto == 'paper':
   print('You win, congrats!')
  elif auto == 'scissors':
   print('We tie')
 auto = random.choice(['rock','paper','scissors'])
 
 user = input('Please input rock, paper, scissors or quit: ')
if user == 'quit':
 print('See you next time')
else:
 print('You should input rock, paper, scissors or quit only')


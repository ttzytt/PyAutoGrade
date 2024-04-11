


import random

random.seed()

r = random.randint(1,10)
print('If you wish to exit the game, input quit instead of rock, paper of scissors')

user = input('Please input rock, paper, scissors or quit: ')

auto = random.choice(['paper','rock','scissors'])


while user == 'rock'or user == 'paper' or user == 'scissors':
 if r == '1':
 
  if user == 'rock':
   print('I choose paper')
   print('I win, haha!')
  elif user == 'paper':
   print('I choose scissors')
   print('I win, haha!')
  elif user == 'scissors':
   print('I choose rock')
   print('I win, haha!')
  else:
   print('You should only input rock, paper or scissors')
 else:
 
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
  else:
   print('You should only input rock, paper or scissors')
 auto = random.choice(['rock','paper','scissors'])
 
 user = input('Please input rock, paper, scissors or quit: ')

if user == 'quit':
 print('See you next time')





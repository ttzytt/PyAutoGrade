




import random

random.seed()

user = input('Enter paper, rock or scissors ')
auto = random.choice(['paper','rock','scissors'])


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
 print('You should input rock, paper or scissors only')

"""
Principle of Computer Science-Period 3

"""

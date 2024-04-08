



print('This time we are going to gamble! You have $50 initially, you will gain $10 if you win a game and lose $10 if you lose a game, if you draw the game you neither gain nor lose, input quit if you wish to exit')
import random

random.seed()

user = input('Enter paper, rock, scissors or quit: ')
auto = random.choice(['paper','rock','scissors'])
bonus = 50

print('I choose '+ auto)

while user == 'rock' or user == 'paper' or user == 'scissors':
 if bonus > 10:
 
  if user == 'paper':
   if auto == 'scissors':
    print('I win, haha!')
    bonus = bonus-10
    
    print('You now have $'+ str(bonus))
    print()
   elif auto == 'rock':
    print('You win, congrats!')
    bonus = bonus+10
    
    print('You now have $'+ str(bonus))
    print()
   elif auto == 'paper':
    print('We tie')
    
    print('You now have $'+ str(bonus))
    print()
  elif user == 'rock':
   if auto == 'paper':
    print('I win, haha!')
    bonus = bonus-10
    print('You now have $'+ str(bonus))
    print()
   elif auto == 'scissors':
    print('You win, congrats!')
    bonus = bonus+10
    print('You now have $'+ str(bonus))
    print()
   elif auto == 'rock':
    print('We tie')
    print('You now have $'+ str(bonus))
    print()
  elif user == 'scissors':
   if auto == 'rock':
    print('I win, haha!')
    bonus = bonus-10
    print('You now have $'+ str(bonus))
    print()
   elif auto == 'paper':
    print('You win, congrats!')
    bonus = bonus+10
    print('You now have $'+ str(bonus))
    print()
   elif auto == 'scissors':
    print('We tie')
    print('You now have $'+ str(bonus))
    print()
  else:
   print('You should input rock, paper, scissors or quit only')
  user = input('Input rock, paper, scissors or quit: ')
 elif bonus == 10:
 
  if user == 'paper':
   if auto == 'scissors':
    print('I win, haha!')
    bonus = bonus-10
    print('You now have $0 and you can\'t play anymore')
    # Game will end if no more bonus is available ($0)
    user = 'quit'
    # User = quit (automatically exit the game)
   elif auto == 'rock':
    print('You win, congrats!')
    bonus = bonus+10
    print('You now have $'+ str(bonus))
    print()
    user = input('Input rock, paper, scissors or quit: ')
   elif auto == 'paper':
    print('We tie')
    print('You now have $'+ str(bonus))
    print()
    user = input('Input rock, paper, scissors or quit: ')
  elif user == 'rock':
   if auto == 'paper':
    print('I win, haha!')
    bonus = bonus-10
    print('You now have $0 and you can\'t play anymore')
    user = 'quit'
   elif auto == 'scissors':
    print('You win, congrats!')
    bonus = bonus+10
    print('You now have $'+ str(bonus))
    print()
    user = input('Input rock, paper, scissors or quit: ')
   elif auto == 'rock':
    print('We tie')
    print()
    print('You now have $'+ str(bonus))
    user = input('Input rock, paper, scissors or quit: ')
  elif user == 'scissors':
   if auto == 'rock':
    print('I win, haha!')
    bonus = bonus-10
    print('You now have $0 and you can\'t play anymore')
    user = 'quit'
   elif auto == 'paper':
    print('You win, congrats!')
    bonus = bonus+10
    print('You now have $'+ str(bonus))
    print()
    user = input('Input rock, paper, scissors or quit: ')
   elif auto == 'scissors':
    print('We tie')
    print('You now have $'+ str(bonus))
    print()
    user = input('Input rock, paper, scissors or quit: ')
  else:
   print('You should input rock, paper, scissors or quit only')
  
 auto = random.choice(['paper','rock','scissors'])
 # Redefine the random choice so that the same input may lead to different outcome in the next round

if user == 'quit':
# Quit will be triggered if the user selected quit or bankrupted
 print('See you next time')
 # Quit the game isn't reversible
 
else:
 print('You should input rock, paper, scissors or quit only')


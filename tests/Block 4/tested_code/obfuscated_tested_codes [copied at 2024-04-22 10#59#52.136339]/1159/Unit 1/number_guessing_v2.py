



import random

random.seed()


auto = random.randint(1,10)

user = int(input('Randomly input an integral between 1 and 10: '))

if user <= 10 and user >= 1:
 while user < auto or user > auto:
 
  if user < auto:
   print('Your answer is too low, try again!')
  elif user > auto:
   print('Your answer is too high, try again!')
  if auto % 2 == 0: 
   print('Hint: that\'s an even number')
  elif auto % 2 == 1: # Odd number
   print('Hint: that\'s an odd number')
  if user <= 0 or user >= 11:
   print('You should input numbers between 1 and 10 ONLY')   
  print()
  user = int(input('Randomly input an integral between 1 and 10: '))
 if user == auto:
  print('You are right, congrats!')
  
else:
 print('You should input numbers between 1 and 10 ONLY')
 




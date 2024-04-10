


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
  print()
  user = int(input('Randomly input an integral between 1 and 10: '))
 if user == auto:
  print('You are right, congrats!')
  
else:
 print('You should input numbers between 1 and 10 ONLY')
 
 print()
 print('Try again, guess a number!')
 user = int(input('Randomly input an integral between 1 and 10: '))











 

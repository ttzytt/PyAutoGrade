



import random

random.seed()

auto = random.randint(1,10)
n = auto
user = int(input('Randomly input an integral between 1 and 10: '))

if user < 1 or user > 10:
 print('Your number should be between 1 and 10')

else:
 while user < n:
  print('Your answer is too low')
  user = int(input(''))
 while user > n:
  print('Your answer is too high')
  user = int(input(''))
 if user == n:
  print('You are right, congrats!')
  
 

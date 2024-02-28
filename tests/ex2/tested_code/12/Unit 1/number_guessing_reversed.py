






print('In this program, you will input')
print('a number from 1 to 10 and I will')
print('ask you a few questions about it,')
print('input \'y\' for yes & \'n\' for no')
print()

user = int(input('Enter a number: '))
print()


if user <= 10 and user >= 1:
 odd = input('Is that an odd number? ')
 if odd == 'y' or odd == 'Y':
 
  prime = input('Is that a prime number? ')
  if prime == 'y' or prime == 'Y':
  
   di3 = input('Can it be divided by 3? ')
   if di3 == 'y' or di3 == 'Y':
    print('Your input is 3') 
   elif di3 == 'n' or di3 == 'N':
   
    di5 = input('Can it be divided by 5? ')
    if di5 == 'y' or di5 == 'Y':
     print('Your input is 5') 
    elif di5 == 'n' or di5 == 'N':
     print('Your input is 7') 
  elif prime == 'n' or prime == 'N':
  
   di3 = input('Can it be divided by 3? ')
   if di3 == 'y' or di3 == 'Y':
    print('Your input is 9') 
   elif di3 == 'n' or di3 == 'N':
    print('Your input is 1') 

 if odd == 'n' or odd == 'N':
 
  greater7 = input('Is that greater than 7? ')
  if greater7 == 'y' or greater7 == 'Y':
  
   di5 = input('Can it be divided by 5? ')
   if di5 == 'y' or di5 == 'Y':
    print('Your input is 10') 
   elif di5 == 'n' or di5 == 'N':
    print('Your input is 8') 
  elif greater7 == 'n' or greater7 == 'N':
  
   prime = input('Is that a prime number? ')
   if prime == 'y' or prime == 'Y':
    print('Your input is 2') 
   elif prime == 'n' or prime == 'N':
   
    di3 = input('Can it be divided by 3? ')
    if di3 == 'y' or di3 == 'Y':
     print('Your input is 6') 
    elif di3 == 'n' or di3 == 'N':
     print('Your input is 4') 
     
else:
 print('Your input should between 1 and 10')

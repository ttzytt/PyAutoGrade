




def factorial(n):
    x = n-1
    while x > 0:
     n = n*x
     x -= 1 
    return n

def triangular_number(n):
    x = n-1
    while x > 0:
     n = n+x
     x -= 1 
    return n

def new_triangular_number(n):
 if n % 2 == 0: 
  x = n-2
  while x > 0:
   n = n+x
   x -= 2
  return n 
 else: 
  x = n-2
  while x > 0:
   n = n+x
   x -= 2
  return n 

n = int(input('Enter an integral: '))
print(str(n) + '! is ' + str(factorial(n)))
print('The triangular number of ' + str(n) + ' is ' + str(triangular_number(n)))
print('The "New" triangular number of ' + str(n) + ' is ' + str(new_triangular_number(n)))


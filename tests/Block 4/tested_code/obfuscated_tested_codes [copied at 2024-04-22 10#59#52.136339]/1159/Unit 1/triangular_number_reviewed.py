






print('The triangular number of n stands for the value of 1+2+3+...+n')
print('In this program we are going to show you how it works')


user = int(input('Please input an integral: '))

answer = user

x = 1

if user > 0:

 while x < user:
  answer = answer+x
  
  x = x+1
  
  print(answer)
else:
 print('Only positive number is accepted')

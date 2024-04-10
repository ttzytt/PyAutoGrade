


print('The triangular number of n stands for the value of 1+2+3+...+n')
print('In this program we are going to show you how it works')


user = int(input('Please input an integral: '))

answer = user

x = 1

if user > 1:

 while x < user:
  
  print(str(answer) + '+' + str(x) + '=')
  
  answer = answer+x
  
  x = x+1
  
  print(answer)
  

elif user == 1:
 print('The triangular number of 1 is 1')
  
else:
 print('Only positive number is accepted')

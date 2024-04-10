


print('Suggest n is an integral, then n! = 1*2*3*...*(n-1)*n')
print('In this program, I will show you how this works')


user = int(input('Input a postive integral: '))

answer = user


x = 1

if user > 1:

 while x < user:
 
  print(str(answer) + '*' + str(x) + '=')
  
  answer = answer*x
  x = x+1
  
  print(answer)
  

elif user == 1:
 print('n! doesn\'t apply to number one')

else:
 print('Only positive number is accepted')

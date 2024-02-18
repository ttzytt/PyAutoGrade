









import random

answer = input('Enter a integer between 1 to 10 ')

computer_choice = random.randint(1,10)






while not int(answer) == int(computer_choice):
     
     
     if int(answer) < int(computer_choice):
          
         print('input a bigger integer')
         
     
     
     elif int(answer) > int(computer_choice):
         print('input a smaller integer')

     answer = input('Enter a integer between 1 to 10 ')






print('Your guessing is right, nice job!')
     
     

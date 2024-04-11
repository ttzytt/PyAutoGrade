


import random


Answer = input("Enter 'rock' or 'paper' or 'scissors' ")











computer_choice = random.randint(0, 9)


if computer_choice == 0:

   
   if Answer == 'rock':
      print('I choose paper.')
      print('I win.')

   if Answer == 'paper':
      print('I choose scissors.')
      print('I win.')

   if Answer == 'scissors':
      print('I choose rock.')
      print('I win.')

else: 

   
    Answer = input("Enter 'rock' or 'paper' or 'scissors' ")

    
    
    computer_choice = random.randint(1,3)


    if computer_choice == 1:
        print('I choose rock.')
    if Answer == 'rock':
        print('We tie.')
    if Answer == 'paper':
        print('You win.')
    if Answer == 'scissors':
        print('I win.')


    elif computer_choice == 2:
        print('I choose paper.')
    if Answer == 'rock':
        print('I win.')
    if Answer == 'paper':
        print('We tie.')
    if Answer == 'scissors':
        print('You win.')


    else:
        print('I choose scissors.')
        if Answer == 'rock':
            print('You win.')
        if Answer == 'paper':
            print('I win.')
        if Answer == 'scissors':
            print('We tie.')






import random

random.seed()

answer = input("Enter 'rock' or 'paper' or 'scissors' ")



computer_cheating_choice = random.randint(0, 9)



if computer_cheating_choice == 0:

   
   if answer == 'rock':
      print('I choose paper.')
      print('I win.')

   if answer == 'paper':
      print('I choose scissors.')
      print('I win.')

   if answer == 'scissors':
      print('I choose rock.')
      print('I win.')

else: 

    computer_answer = random.randint(1,3)



    if computer_answer == 1:
        print('I choose rock.')
        if answer == 'rock':
           print('We tie.')
        if answer == 'paper':
           print('You win.')
        if answer == 'scissors':
           print('I win.')



    elif computer_answer == 2:
        print('I choose paper.')
        if answer == 'rock':
           print('I win.')
        if answer == 'paper':
           print('We tie.')
        if answer == 'scissors':
           print('You win.')



    else:
        print('I choose scissors.')
        if answer == 'rock':
            print('You win.')
        if answer == 'paper':
            print('I win.')
        if answer == 'scissors':
            print('We tie.')


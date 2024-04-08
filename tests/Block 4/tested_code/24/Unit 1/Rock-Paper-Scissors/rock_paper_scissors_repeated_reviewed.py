



import random

random.seed()

print('This is a rock paper scissors game. Enter \'quit\' if you want to stop')

user_choice = input('Enter \'rock\' \'paper\' or \'scissors\': ')
computer_rps_choice = random.choice(['rock', 'paper', 'scissors'])


while ((user_choice.lower() == 'rock') or
       (user_choice.lower() == 'paper') or
       (user_choice.lower() == 'scissors')):

        if(user_choice == computer_rps_choice):
            
            print('I played ' + computer_rps_choice + '! Draw!')
            
        elif((computer_rps_choice =='rock' and user_choice == 'scissors')
             or (computer_rps_choice =='scissors' and user_choice == 'paper')
             or (computer_rps_choice =='paper' and user_choice == 'rock')):
            

            print('I played ' + computer_rps_choice + '! I win!')
            
        else: 
            print('I played ' + computer_rps_choice + '! You win! Good game!')

        user_choice = input('Enter \'rock\' \'paper\' or \'scissors\': ')
        computer_rps_choice = random.choice(['rock', 'paper', 'scissors'])

if(user_choice == 'quit'):
    print( )

else:
    print('You incompetent doofus.')





import random

random.seed()

user_rp_choice = input('Enter \'rock\' or \'paper\': ')

num = random.randint(1,2) 
if (num == 1):
    computer_rp_choice = 'rock' 
elif (num == 2):
    computer_rp_choice = 'paper' 


if(user_rp_choice == 'rock') or (user_rp_choice == 'paper'):
    print('I choose ' + computer_rp_choice + '.') 

    if(computer_rp_choice == user_rp_choice): 
        print('We tie.')
    elif(computer_rp_choice == 'paper') and (user_rp_choice == 'rock'): 
        print('I win.')
    elif(computer_rp_choice == 'rock') and (user_rp_choice == 'paper'): 
        print('You win.')


elif(user_rp_choice == 'scissors') or (user_rp_choice == 'Scissors'):
    print('Yay, you win!!!!! Oh wait no. . .  You lost because of your stupidity. You didn\'t even read directions well enough to tell that it said to enter \'rock\' or \'paper\'. A baby would have done better.')

else:
    print('Come on dude. You need to wisen up and read directions.')
          
    

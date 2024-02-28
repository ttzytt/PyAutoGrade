

import random
import time

random.seed()
print("Let's play rock paper")
time.sleep(1)
p_choice = input("Enter 'rock' or 'paper'(all lowercase, no spaces): ")
time.sleep(1)



if p_choice == 'paper' :
    p_choice = 1
elif p_choice =='rock':
    p_choice = 0

c_choice = random.randint(0,1)

if p_choice != 1 and 0:
    time.sleep(0.5)
    print("that's not rock or paper")
    time.sleep(0.5)
    print('learn how to read')

elif p_choice > c_choice:
    time.sleep(1)
    print()
    time.sleep(0.5)
    print('You win.')

elif p_choice == c_choice:
    if c_choice == 1:
        time.sleep(1)
        print()
        time.sleep(0.5)
        print()
    else:
        time.sleep(1)
        print()
        time.sleep(0.5)
        print('We tie')
else:
    time.sleep(1)
    print()
    time.sleep(0.5)
    print('You lose')









import random

random.seed()

user_guess = int(input('Input a number: '))
computer_number = random.randint(1,10) 
count = 1

while(user_guess != computer_number): 
    if (user_guess > computer_number): 
        print('That\'s too high!')
    else: #If not too high, too low
        print('That\'s too low :( ')
        
    if (12 > count > 10):
        print()

        
    print()
    user_guess = int(input('Input a number: ')) 

    count += 1

print()



import random

random.seed()

user_guess = int(input('Input a number: '))
computer_number = random.randint(1,100) 
count = 1


while(user_guess != computer_number): 
    if (user_guess > computer_number): 
        print('That\'s too high!')
    else: # If not too high, too low
        print('That\'s too low :( ')
    if(count == 5): 
        if(computer_number % 2 == 0): 
            print('Hint: the number is even!')
        else: 
            print('Hint: The number is odd!')
    elif(count == 10): 
        if(computer_number > 9):
            sum_of_numbers = int(str(computer_number)[0]) + int(str(computer_number)[1])
        else:
            sum_of_numbers = int(str(computer_number)[0])
        print('Hint: The sum of the digits are ' + str(sum_of_numbers))
    elif (count == 101):
        print()

        
    print()
    user_guess = int(input('Input a number: ')) 

    count += 1

print()
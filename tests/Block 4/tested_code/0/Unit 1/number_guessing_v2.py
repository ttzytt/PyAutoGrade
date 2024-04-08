
import random

player_input =int(input('Please select a number 1 - 30 (The computer will tell you if the computer input is even or odd if you do not guess it on the first time): '))

computer_input =  random.randrange(1,30)


if computer_input == 10 or computer_input == 20 or computer_input == 30:
    if (computer_input%2) == 0:
        print('The number is even')
    else:
        print('The number is odd')
if computer_input == 5 or computer_input == 15 or computer_input == 25:
    if computer_input%5 == 0:
        print('Number is divisible by 5')
    else:
        print('Number is not divisible by 5')
if computer_input == 7 or computer_input == 16 or computer_input == 23:
    triangular_number = 0
    while computer_input > 0:
        triangular_number = triangular_number + computer_input
        computer_input =  computer_input - 1
    print(triangular_number)




if player_input > (30) or player_input < 0:
            print('Your number is not within the 1-30 range. ')
            player_input = int(input('Please select a number 1-30: '))

while player_input != computer_input:
    if (player_input) > (computer_input):
        print('Too high')
        player_input = int(input('Enter another number: '))
    elif (player_input) < (computer_input):
        print('Too low')
        player_input = int(input('Enter another number: '))
                
else: 
    print('You got it!')

    
    

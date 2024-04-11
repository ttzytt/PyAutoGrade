import random
player_input = int(input('Please select a number 1 - 10: '))
computer_input =  random.int([1,2,3,4,5,6,7,8,9,10])

while computer_input != player_input:
    computer_input = input('Is the number odd: ')
    if computer_input == 'yes':
        player_input%2 != 0
    else:
        player_input%2 == 0
    computer_input = input('Is the number divisible by 5: ')
    if computer_input == 'yes':
        player_input%5 == 0
        
         
    else:
        player_input%5 != 0
       
    
    if computer_input == player_input:
        print('you got it')
    elif computer_input != player_input:
        print('nope')





import random
print('Enter a amount of money and if you get a higher value than the computer you get the bet amount added to your money.')
money_amount = 100 
play_again = 'yes' 

while play_again == 'yes' or no_play_again == 'no':

    bet_amount = int(input('Please enter the amount of money you want to bet: '))
    
    card = ['diamonds', 'spades', 'hearts', 'clubs']
    value = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    no_play_again = 'yes'
    human_input_value = random.choice(value)
    human_input_card = random.choice(card)
    print('You chose the '+ str(human_input_value) + ' of ' + str(human_input_card) + '.')
    

    value = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    card = ['diamonds', 'spades', 'hearts', 'clubs']
    computer_input_value = random.choice(value)
    computer_input_card = random.choice(card)
    print('I chose the '+ str(computer_input_value) + ' of ' + str(computer_input_card) + '.')
    
    new_money_amount = money_amount + bet_amount   
    lost_amount = money_amount - bet_amount
    

    if human_input_value > computer_input_value:
        print('You win')
        print('You now have ' + str(new_money_amount) +' $.')
        money_amount = new_money_amount
    

    elif human_input_value < computer_input_value:
        print('I win')
        if money_amount - bet_amount <= 0:
            print('You ran out of money')
        print('You now have ' + str(lost_amount) +'$.')
        money_amount = lost_amount

    elif human_input_value == computer_input_value:
        print('We tie')
        print('You now have ' + str(money_amount) + '$.')

    if money_amount - bet_amount >= 0:      
        play_again = input('To play again type yes, to quit type quit: ')
    elif money_amount - bet_amount <= 0:
        play_again = 'no'
print('Bye bye')


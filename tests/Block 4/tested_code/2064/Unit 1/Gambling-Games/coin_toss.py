


import random

random.seed()

print('''This is a coin toss game. You can bet money, and if you win you get the
amount that you bet, but if you lose you lose that money. You can take out loans
from the bank, with a 0.05% interest rate each time you play. To stop playing,
enter quit when the game prompts you for 'Heads or tails?'. Have fun!

''')

user_money_amount = 100


user_bet_choice = int(input('How much would you like to bet? '))
amount_of_loans = 0 
user_coin_choice = input('Heads or tails? ') 
loans = input('Would you like to be able to take out loans? ') 




if(user_bet_choice > user_money_amount) and (loans.lower() != 'yes'):
    print('I\'m sorry, you don\'t have enough money. Game over.') 
    user_coin_choice = 'quit' 





while ((user_coin_choice.lower() == 'heads') or
       (user_coin_choice.lower() == 'tails')):
    flip_outcome = random.choice(['heads', 'tails']) 


    
    if(user_bet_choice > user_money_amount) and (loans.lower() != 'yes'):
        print('I\'m sorry, you don\'t have enough money. Game over.') 
        user_coin_choice = 'quit' 

    
    elif((user_bet_choice > user_money_amount) and (loans.lower() == 'yes')
       and (user_coin_choice.lower() != flip_outcome)):
        amount_of_loans += user_bet_choice - user_money_amount 
        user_money_amount = 0 
        user_coin_choice = input('Heads or tails? ') 
        
    
    elif(user_coin_choice.lower() == flip_outcome):
        print('Congratulations you won! You get $' + str(user_bet_choice))
        user_money_amount += user_bet_choice 

    
    else:
        print('I picked ' + flip_outcome + ' Awwwww. . .  You lost $' + str(user_bet_choice))
        user_money_amount -= user_bet_choice 

    

    

    
    user_bet_choice = int(input('How much would you like to bet? ')) 
    
    

    

    
    user_coin_choice = input('Heads or tails? ')


print('The amount of money in your account is: $' + str(user_money_amount))
print('The amount of money you owe is: $' + str(format(amount_of_loans, 'f')))
        
        
    


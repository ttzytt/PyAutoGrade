




import random
money = 100


coin = input('choose heads or tails: ')

while money > 0 and coin != 'quit':
 
    bet = int(input('put a bet: '))


    result = random.choice(['heads','tails'])

    if coin == result:
        print('correct, you won ' + str(bet))
        money += bet
    elif coin != result:
        print('incorrect, you lost ' + str(bet))
        money -= bet

    print('You have $' + str(money) + ' right now.')

    
    coin = input('choose heads or tails: ')
        
if money <= 0:
    print('you are out of money')


        

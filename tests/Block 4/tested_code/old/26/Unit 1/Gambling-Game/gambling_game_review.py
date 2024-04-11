



import random
random.seed()


response = 'a'


money = 100

while response != 'quit' and money >= 0:
    print()
    human = input('Enter paper, scissors or rock: ')
    computer = random.choice(['paper', 'rock', 'scissors'])
    print()
    money_bet = int(input("How many money you want to bet: "))
    print()

    
    print('I choose ' + computer + '.')

    if human == computer: 
        print ('We tie.')
    elif human == 'paper': 
        if computer == 'rock':
            print('You win.')
            money = money + money_bet
        else:
            print('I win.')
            money = money - money_bet

    elif human == 'scissors': 
        if computer == 'rock':
            print('I win.')
            money = money - money_bet
        else:
            print('You win.')
            money = money + money_bet   
    else:    
        if computer == 'paper':
            print('I win.')
            money = money - money_bet
        else:
            print('You win.')
            money = money + money_bet

    
    print()
    print('Money:' + str(money))
    
    if money < 0:
        
        print('The game is over.')
    else:
        
        print()
        response = input('Type quit to stop the game: ')
        print()




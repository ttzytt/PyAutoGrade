


import random



playerinput = input('Enter rock, paper, scissors, or quit: ')
random.seed()


while playerinput != 'quit':
    
    
    botchoice = random.choice(['rock', 'paper', 'scissors'])
    print('I chose ' + botchoice)

    
    
    if playerinput == 'rock':
        if botchoice == 'rock':
            print('We tied.')
        elif botchoice == 'paper':
            print('I won!')
        elif botchoice == 'scissors':
            print('You won!')

    elif playerinput == 'paper':
        if botchoice == 'paper':
            print('We tied.')
        elif botchoice == 'scissors':
            print('I won!')
        elif botchoice == 'rock':
            print('You won!')

    elif playerinput == 'scissors':
        if botchoice == 'scissors':
            print('We tied.')
        elif botchoice == 'rock':
            print('I won!')
        elif botchoice == 'paper':
            print('You won!')
            
    
    else:
        print('Invalid choice: type rock, paper, or scissors!')

    
    playerinput = input('Enter rock, paper, scissors, or quit ')



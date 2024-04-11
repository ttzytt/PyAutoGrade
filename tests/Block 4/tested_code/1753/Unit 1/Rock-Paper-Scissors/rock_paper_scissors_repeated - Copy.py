


player = input('Choose rock, paper, or scissors: ') 

while player.lower() == 'rock' or player.lower() == 'paper' or player.lower() == 'scissors':
    
    import random

    random.seed()

    computer = random.choice(['rock', 'paper', 'scissors'])
        

    if player.lower() == computer: 
        print('I choose ' + player.lower() + '.')
        print('We tied')

    elif computer == 'rock': 
        print('I choose rock.')
        if player.lower() == 'paper':
            print('You win!')
        else:
            print('You lose!')
    
    elif computer == 'paper': 
        print('I choose paper')
        if player.lower() == 'scissors':
            print('You win!')
        else:
            print('You lose!')

    elif computer == 'scissors': 
        print('I choose scissors')
        if player.lower() == 'rock':
            print('You win')
        else:
            print('You lose')

    print() 
    player = input('Choose rock, paper, scissors, or quit (to leave the game): ')
   
if player.lower() == 'quit': 
    print('Sorry to see you go. have a nice day!')

else: 
        print('Try again.')

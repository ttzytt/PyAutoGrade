



import random
random.seed()

response = 'a' 
while response != 'quit':
    print()
    probability = random.randint(1,10) 
    if probability != 1:
        human = input('Enter paper, scissors or rock: ')
        computer = random.choice(['paper', 'rock', 'scissors'])

        
        print()
        print('I choose ' + computer + '.')

        
        if human == computer: 
            print('We tie.')
        elif human == 'paper': 
            if computer == 'rock':
                print('You win.')
            else:
                print('I win.')
        elif human == 'scissors': 
            if computer == 'rock':
                print('I win.')
            else:
                print('You win.')   
        else: 
            if computer == 'paper':
                print('I win.')
            else:
                print('You win.')


    else: 
        
        print()
        if human == 'paper':
           print('I choose scissors.')
        elif human == 'rock':
           print('I choose paper.')
        else:
           print('I choose rock.')

        
        
        print('I win.')
        
    
    print()
    response = input('Type quit to stop the game: ')






import random
random.seed()


response = 'a'


while response != 'quit':
    print()
    human = input('Enter paper, scissors or rock or "q" to quit: ')
    computer = random.choice(['paper', 'rock', 'scissors'])

    
    print()
    if human != 'q':
        
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
        break

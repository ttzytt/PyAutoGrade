


import random



playerinput = input('Enter rock or paper: ')
random.seed()



botchoice = random.choice(['rock', 'paper'])
print('I chose ' + botchoice)



if playerinput == 'rock' and botchoice == 'rock':
    print('We tied!')
elif playerinput == 'rock' and botchoice == 'paper':
    print('I won!')
elif playerinput == 'paper' and botchoice == 'paper':
    print('We tied!')
elif playerinput == 'paper' and botchoice == 'rock':
    print('You won!')
else:
    print('Invalid choice; type rock or paper!')



    

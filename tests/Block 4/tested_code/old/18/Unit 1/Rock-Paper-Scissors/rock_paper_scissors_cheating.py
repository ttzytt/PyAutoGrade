





player = input("Enter 'rock', 'paper' or 'scissors': ")


if player == 'rock':
    print ('I chose paper')
    print ('I win')
elif player == 'paper':
    print ('I chose scissors')
    print ('I win')
elif player == 'scissors':
    print ('I chose rock')
    print ('I win')
else:              
    print( player + ' is not one of the options. Please choose rock or paper.')

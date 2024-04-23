


player = input("Enter 'rock', 'paper' or 'scissors': ")


if player == 'rock':
    computer = 'paper.'
    print("I choose " + computer)
    print ('I win.')
    

elif player == 'paper':
    computer = 'scissors.'
    print("I choose " + computer)
    print ('I win.')

elif player == 'scissors':
    computer = 'rock.'
    print("I choose " + computer)
    print ('I win.')


else:
    print("Silly! That's not rock paper scissors! :(")

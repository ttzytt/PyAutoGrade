



import random

random.seed()

print("Hello and welcome to 'Man V. Mainframe', a game where both you and the computer place"\
    +" a bet on a number between 1 and 2. Whoever guesses correctly gets the other person's"\
    +' bet until one of the players runs out of money or forfeits. Let the games begin!')
print('Human, which number do you bet on and how much do you bet?')

playermoney = 100
computermoney = 100

print('You have $' + str(playermoney) + '.')
gamestart = 1
while gamestart == 1:
    playernum = int(input('Number(1 or 2):'))
    playerbet = int(input('Bet:'))
    
    computernum = random.choice([1,2])
    computerbet = random.choice([10,20,30])
    randomnum = random.choice([1,2])
    
    print('I bet $' + str(computerbet))
    accept = input('Do you accept?')
    if accept == 'Yes'or accept == 'yes':
        print("Let's begin.")
        print('The number was ' + str(randomnum))
        
        if randomnum == computernum:
            print('You lose $' + str(playerbet))
            computermoney + computerbet + playerbet
            playermoney = playermoney - playerbet
            print('You now have $' + str(playermoney))
            

            if playermoney <= 0:
                print("You're out of money!")
                gamestart = 0 
            else:
                print("Let's play again")


        elif randomnum == playernum:
            print('You win $' + str(computerbet))
            playermoney = playermoney + computerbet
            print('You now have $' + str(playermoney))
            print("Let's play again")
            
        else:
            print('Neither of you guessed the number!')

    else:
        gamestart = 0
        print('Game over!')







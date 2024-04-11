



import random

random.seed()


print('The name of the game is "Which is Bigger?" You have a deck of cards'\
      +' and I have a deck of cards. A random card will be selected from both.'\
      +' You will bet a certain amount, and if your card has more value, then' \
      +' you win the money, but if my card has more value, then you lose that'\
      +' money(face cards are not included). You start with $100.')

money = 100
want = 'sure'
while want != 'QUIT' and money > 0:
    
    computer = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    player = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    bet = int(input('How much do you want to bet?'))
    
    
    
    if player > computer:
          print('You win!')
          money = money + bet
    elif player < computer:
          print('You lose!')
          money = money - bet
    else:
          print('We tie! Nothing happens')

    
    print( 'My card was: ' + str(computer))
    print( 'Your card was: ' + str(player))

    print('You have: ' + str(money) + '$.')

    
    want = input('Do you want to keep playing(type QUIT if you wish to stop)?')


if money < 0:
    print("You ran out of money")

elif want == QUIT:
    
    print("Thanks for playing, your final amount was: " + money)
    

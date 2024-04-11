





import random

random.seed()


player = str(input("Enter rock or paper: "))


bot = random.choice(['rock' , 'paper'])


if player == 'rock' and bot == 'paper':
    print('I choose paper.')
    print('You lose!')
elif player == 'paper' and bot == 'rock':
    print('I choose rock.')
    print('You win!')
elif player == bot:
    print('We both chose ' + player + '.')
    print('We tie!')
else:
    print('Please choose rock or paper')

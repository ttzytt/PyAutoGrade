



import random
random.seed()


human = input('Enter rock or paper: ')
computer = random.choice(['paper', 'rock'])


print()


print('I choose ' + computer + '.')


if human == computer:
    print('We tie.')
elif human == 'paper':
    print('You win.')
else:
    print('I win.')


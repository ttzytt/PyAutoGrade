



print('In this program, we are going to play')
print('rock paper scissors, here are the rules:')
print()
print('Your result will be showed in bonus.')
print('You can input \'q\' to exit.')
print('If you input something wrong, you may')
print('resume your game, so don\'t worry!')
print('Now let\'s get started, are you ready?')
print()


def result(bonus,client,auto):

    while client != 'q':

     if ((client == 'rock' and auto == 'rock')

             or (client == 'paper' and auto == 'paper')
             or (client == 'scissors' and auto == 'scissors')):
         return bonus
     elif ((client == 'rock' and auto == 'scissors')
             or (client == 'paper' and auto == 'rock')
             or (client == 'scissors' and auto == 'paper')):
         bonus = bonus+1
         return bonus
     elif ((client == 'rock' and auto == 'paper')
             or (client == 'paper' and auto == 'scissors')
             or (client == 'scissors' and auto == 'rock')):
         bonus = bonus-1
         return bonus
     else:
         print('Please enter rock, paper, scissors or quit ONLY')
         return bonus


     auto = random.choice(['rock','paper','scissors'])
     client = input('Enter rock, paper, scissors or quit: ')


bonus = 0
import random
random.seed()
client = input('Enter rock, paper, scissors or quit: ')
while client != 'q':

    auto = random.choice(['rock','paper','scissors'])
    bonus = result(bonus,client,auto)
    print(bonus)

    print()

    client = input('Enter rock, paper, scissors or quit: ')

if client == 'q':


    print('See you next time')


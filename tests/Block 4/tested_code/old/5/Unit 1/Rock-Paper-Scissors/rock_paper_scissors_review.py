

import random
import time
random.seed()


print("Hello, lets play a game of rock paper scissors.")

time.sleep(1)

player = input("Choose one: Rock or Paper? (all lowercase)")

computer = random.choice(['rock', 'paper', 'scissors'])
      
print("I choose " + computer + ".")


if str(computer) == str(player):
    print("Looks like we tied, want to play again?")

if str(computer) == ('rock'):
    if str(player) == ('paper'):
        print("Looks like I lost, Good Game!")

    elif str(player) == ('scissors'):
        print("I win gg ez.")

if str(computer) == ('paper'):
    if str(player) == ('rock'):
        print("Looks like I lost, Good Game!")
    elif str(player) == ('scissors'):
        print("I win gg ez.")

if str(computer) == ('scissors'):
    if str(player) == ('rock'):
       print("Looks like I lost, Good Game!")
    elif str(player) == ('paper'):
        print("I win gg ez.")






import random
import time

random.seed()

print("Hello, lets play a game of rock and paper.")


time.sleep(2)

print("Choose one: Rock or Paper?")

time.sleep(2)


computer = random.choice(['rock', 'paper'])


player = input("What do you choose? (all lowercase)")

print("I choose " + computer + ".")



if str(computer) == str(player):
    print("Looks like we tied, want to play again?")

elif str(computer) == ('rock') or str(player) == ('paper'):
    print("Looks like I lost, Good Game!")

elif str(computer) == ('paper') or str(player) == ('rock'):
    print("I win gg ez.")



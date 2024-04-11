


import random

random.seed()

print("Hello, lets play a game of rock and paper.")

player = input("What do you choose? (all lowercase) ")


computer = random.choice(['rock', 'paper'])


print("I choose " + computer + ".")

if str(computer) == str(player):
    print("Looks like we tied, want to play again?")

elif str(computer) == ('rock') or str(player) == ('paper'):
    print("Looks like I lost, Good Game!")

else:
    print("I win gg ez.")



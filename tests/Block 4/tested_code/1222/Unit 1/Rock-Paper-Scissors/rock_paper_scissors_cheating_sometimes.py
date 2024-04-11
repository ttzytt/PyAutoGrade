import random
import time



print("Hello, lets play a game of rock paper scissors.")

time.sleep(1)

player = input("Choose one: Rock or Paper? (all lowercase)")

rock_random = random.choices(['rock', 'paper', 'scissors'], [3,4,3])[0]
paper_random = random.choices(['rock', 'paper', 'scissors'], [3,3,4])[0]
scissors_random = random.choices(['rock', 'paper', 'scissors'], [4,3,3])[0]

print("I choose " + rock_random + ".")
if player == str("rock"):
    print("I choose " + rock_random + ".")
    if str(rock_random) == ('rock'):
        print('Loooks like we tied. Good Game.')
    elif str(rock_random) == ('scissors'):
        print("Looks like I lost, Good Game!")
    else str(rock_random) == ('paper'):
        print("I win gg ez.")

elif player == str("paper"):
    print("I choose " + rock_random + ".")
    if str(paper_random) == ('paper'):
        print('Loooks like we tied. Good Game.')
    elif str(paper_random) == ('rock'):
        print("Looks like I lost, Good Game!")
    else str(paper_random) == ('scissors'):
        print("I win gg ez.")

elif player == str("scissors"):
    print("I choose " + rock_random + ".")
    if str(scissors_random) == ('scissors'):
        print('Loooks like we tied. Good Game.')
    elif str(scissors_random) == ('paper'):
        print("Looks like I lost, Good Game!")
    else str(scissors_random) == ('rock'):
        print("I win gg ez.")





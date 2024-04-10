


import random

random.seed()


print("You are gambling to win in rock paper scissors. You start with $100 and you can bet up to the total amount you have.")
print("You may quit at any time, but you automatically lose when you lose all your money.")
print()


money = 100


ready = input('Ready to play? ').lower()





while money > 0 and ready == 'yes':
    betting_money = int(input('How much money would you like to bet? '))

    if betting_money > money:
        print("You can't bet more than you have. Please enter a valid bet.")
        continue

    print('Okay, now your total is ' + str(money - betting_money) + ' dollars.')
    print()

    user = input("Choose rock, paper, scissors, or quit: ")

    if user == 'quit':
        break

    computer = random.choice(['rock', 'paper', 'scissors'])
    print("I choose... ", computer)

    if user == computer:
        print('We tie. Your bet is returned. You now have: ' + str(money))
    elif (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper') or (user == 'rock' and computer == 'scissors'):
        money += betting_money
        print('You won. You earn double your bet. You now have: ' + str(money))
    else:
        money -= betting_money
        print('I win. You lose your bet. You now have: ' + str(money))


if money <= 0:
    print("You've run out of money. You lost the game.")
elif ready != 'yes':
    print("It's unfortunate you must go...")

print('Hope you come back later!')

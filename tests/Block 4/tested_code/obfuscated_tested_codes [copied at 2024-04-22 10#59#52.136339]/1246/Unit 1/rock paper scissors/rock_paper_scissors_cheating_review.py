




import random

random.seed()


p_choice = input("Enter rock, paper, or scissors, (all lowercase, no spaces): ")



if p_choice == 'rock':
    print('I choose paper')
elif p_choice == 'paper':
    print('I choose scissors')
elif p_choice == 'scissors':
    print('I choose rock')
else:
    print("You didn't type rock, paper, or scissors")
print('I win')

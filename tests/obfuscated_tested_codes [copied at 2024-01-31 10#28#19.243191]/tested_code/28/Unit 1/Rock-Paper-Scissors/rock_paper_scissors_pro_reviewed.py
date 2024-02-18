


import random

random.seed()



def rock_paper_scissors(choice_1, choice_2):
    if choice_1 == choice_2:
        return 0
    elif choice_2 == ('rock'):
        if choice_1 == ('paper'):
            return +1
        elif choice_1 == ('scissors'):
            return -1

    elif choice_2 == ('paper'):
        if choice_1 == ('rock'):
            return -1
        elif choice_1 == ('scissors'):
            return +1

    elif choice_2 == ('scissors'):
        if choice_1 == ('rock'):
           return +1
        elif choice_1 == ('paper'):
            return -1

print("Hello, lets play a game of rock paper scissors.")


point = 0

new_point = point
response = 'yes'


while response == 'yes':

    
    random.seed()
    
    choice_1 = input("Choose one: rock, paper, or scissors? (all lowercase, no spaces) ")
    choice_2 = random.choice(['rock', 'paper', 'scissors'])
    print("I choose " + choice_2 + ".")

    if rock_paper_scissors(choice_1, choice_2) == -1:
        print('I won, gg ez')
        new_point = new_point - 1
        
    elif rock_paper_scissors(choice_1, choice_2) == +1:
        print('Looks like I lost, GG')
        new_point = new_point + 1
        
    elif rock_paper_scissors(choice_1, choice_2) == 0:
        print('We tie')
        
        
        new_point = new_point
        
    
    
    point = new_point
    
    print('You have ' + str(point) + ' points.')

    
    
    
    
    
    response = input("To play again type yes, to quit type q ")
    if response == 'yes':
        response == 'yes'

    elif response == 'q':       
        print("I'm sad to see you go :(")
        print("You total amount of points is " + str(point) + ".")
        response == 'no'
    
    elif response != 'yes' or response != 'q':
        print("Follow instructions boi.")
        
        response = input("Try again.")





import random



amount = 10
answer = 'a'
while answer != 'quit' and amount > 0:

    
    
    
    answer = input("Enter 'rock' or 'paper' or 'scissors' or 'quit'(input quit to stop the game) ")
        
    if answer != 'quit':
        
        
        
        
        
        computer_choice = random.randint(0,2)
        if computer_choice == 0:
            print('I choose rock.')
            if answer == 'rock':
                print('We tie.' )
            elif answer == 'paper':
                print('You win.')
                amount = amount + 1
            else:
                print('I win.')
                amount = amount - 1

        

        elif computer_choice == 1:
            print('I choose paper.')
            if answer == 'rock':
                print('I win.')
                amount = amount - 1
            elif answer == 'paper':
                print('We tie.')
            else:
                print('You win.')
                amount = amount + 1
        
        

        else:
            print('I choose scissors.')
            if answer == 'rock':
                print('You win.')
                amount = amount + 1
            elif answer == 'paper':
                print('I win.')
                amount = amount - 1
            else:
                print('We tie.')
        print("Amount: "+ str(amount))

if amount == 0:
    print('The game ends')



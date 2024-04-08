




import random
random.seed()


print('You have $100 to bet in total. We are playing dice roll now.')
print('I will roll a 6-sided die. If you guess correctly the number, '
      'you will win back 4X the amount you bet. If you guess incorrectly, '
      'you lose your bet.')
print() 


user_quit = 'continue'
user_total = 100 
print('You have $' + str(user_total) + ' now.')
print('Warning, your total CANNOT be negative after you bet')
user_bet = int(input('Enter the amount you want to bet(integer): '))
user_total = user_total - user_bet


while user_quit == 'continue' and user_total >= 0: 

    
    comp_choice = random.randint(1, 6) 
    user_choice = int(input('Enter the number(face) you want to guess (1 to 6): '))

    
    if comp_choice == user_choice:
        print('Congrats! You guessed it correctly!')
        user_total = user_total + 4 * user_bet
    else: 
        print('Oh no! You guessed it wrong...')
    
    print('You have $' + str(user_total) + ' now.')
    user_quit = input("Do you want to keep playing? Enter 'continue' or 'quit': ")

    
    if user_quit == 'continue':
        print()
        print('Warning, your total CANNOT be negative after you bet')
        user_bet = int(input('Enter the amount you want to bet(integer): '))
        user_total = user_total - user_bet
    
       
if user_total < 0: 
    print("We're sorry, you have no money left.")
print('Goodbye.')


        

        

    

    

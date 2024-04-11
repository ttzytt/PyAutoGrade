






    
    
    

    
    
    
    








import random

import time

random.seed()



money = 100


heads_or_tails = 0


play_or_not = 1


loss_count = 0
win_count = 0



print('''
    We will be playing a fun game of coin flipping.
    You will start with 100 dollars, and you can bet from 1 up to how much money u currently have.
    Choose wether you think the coin will land on tails or heads.
    If you choose correctly, you will recieve the amount you bet doubled.
    However, if you choose correctly, you also have an exciting option to double or nothing.
    If you choose to not double or nothing, you will get the amount of bet doubled.
    However, if you choose to double or nothing, and you win,
    you will recieve the amount you bet times four, and each time you win, that amount is doubled.
    However, if at any point, you lose the double or nothing(you can do it multiple times if you keep winning)
    you will not recieve anything.
    
    ''')





def sleep_time(on_off, delay_time):
    if on_off == 1:
        time.sleep(delay_time)
    else:
        time.sleep(0)









on_off = input('Do you want to enable time between outputs(yes/no): ')

if on_off == 'yes':
    on_off = 1
elif on_off == 'no':
    on_off = 0
else:
    print('You did not enter a correct value, time will be off')
    on_off = 0

while money > 0 and play_or_not == 1:

    

    random.seed()

    amount_bet = 0

    sleep_time(on_off, 0.5)

    print()
    print('You have ' + str(money) + ' dollars right now')
    print()

    sleep_time(on_off, 0.8)
    
    while amount_bet  < 1 or amount_bet > money:
        
        amount_bet = int(input('Enter how much money you want to bet(you can bet from one up to how much you have): '))
        
        if amount_bet < 1:
            sleep_time(on_off, 0.5)
            print()
            print('You have to bet more than a dollar')
            print('Enter again')
            print()
            
        elif amount_bet > money:
            sleep_time(on_off, 0.5)
            print()
            print('Haha ur too broke to bet this much')
            print('Enter again')
            print()
    

    
    money -= amount_bet

    sleep_time(on_off, 1)
    
    print()
    player_choice = input('Enter your choice (heads/tails): ')
    print()

    
    if player_choice == 'heads':
        player_choice = 1
    elif player_choice == 'tails':
        player_choice = 0
        
    toss_coin = input('Do you want do flip the coin(yes/no): ')

    if toss_coin == 'yes':
        
        heads_or_tails = random.randint(0,1)
        
        

        sleep_time(on_off, 1 + random.random())
        print()
        print('the coin is flipping...')
        print()
        
        sleep_time(on_off, 1 + random.random())
        
        if heads_or_tails == 0:
            print('The coin flipped to tails')
            
        elif heads_or_tails == 1:
            print('The coin flipped to heads')

        print()

        if player_choice == heads_or_tails:

            sleep_time(on_off, 0.7)
            
            print('You got it!')
            
            
            amount_bet = amount_bet * 2
            print('You will get ' + str(money + amount_bet) + ' dollars')
            print()
            
            win_count += 1

            sleep_time(on_off, 0.5)
            
            double_or_nothing = input('Do you want to double or nothing?(yes/no): ')

            if double_or_nothing == 'no':
                lose_or_choose = 0
                print('Thats okay, take your money')

                
                money = money + amount_bet

            
            while double_or_nothing == 'yes':

                random.seed()
                
                player_choice = input('Enter your choice (heads/tails): ')

                
                if player_choice == 'heads':
                    player_choice = 1
                elif player_choice == 'tails':
                    player_choice = 0
                
                heads_or_tails = random.randint(0,1)
                

                sleep_time(on_off, (1 + random.random()))
                print()
                print('the coin is flipping...')
                print()
                
                sleep_time(on_off, 1 + random.random())
                
                if heads_or_tails == 0:
                    print()
                    print('The coin flipped to tails')
                    print()
                    
                elif heads_or_tails == 1:
                    print()
                    print('The coin flipped to heads')
                    print()
                
                if heads_or_tails == player_choice:
                    
                    sleep_time(on_off, 0.7)
                    
                    print('You got it')
                    amount_bet = amount_bet * 2                   
                    print('You now have ' + str(money + amount_bet) + ' dollars')
                    double_or_nothing = input('double or nothing(yes/no): ')
                    
                    
                    
                    
                    lose_or_choose = 1
                    print()

                    win_count += 1

                
                elif heads_or_tails != player_choice:

                    sleep_time(on_off, 0.7)
                    
                    print('You did not get it')
                    print('You lost ur money')
                    print()
                    print('You now have ' + str(money) + ' dollars')
                    print()
                    
                    
                    lose_or_choose = 0
                    
                    money = money
                    double_or_nothing = 'no'

                    loss_count += 1

            
            
            
            if lose_or_choose != 0:
                money = money + amount_bet
                print("That's okay, take your money")

        
        elif player_choice != heads_or_tails:

            sleep_time(on_off, 0.7)
            
            print('Unfortunately, you did not get it')
            print('You now have ' + str(money) + ' dollars')
            money = money

            loss_count += 1       
    
    elif toss_coin == 'no':

        sleep_time(on_off, 0.5)
        
        print("I'll be taking your money then")
        money = money

    sleep_time(on_off, 0.5)
    
    print()
    play_or_not = input("If you want to quit, enter 'quit', and enter 'again' to play again: ")
    print()
    
    if play_or_not == 'quit':
        play_or_not = 0
    elif play_or_not == 'again':
        play_or_not = 1

sleep_time(on_off, 1)



if money > 0:
    print('Sorry to see you go, all ur money will be wiped :)')
    print('Here are your wins and losses and ur win/loss ratio: ')
    
    sleep_time(on_off, 1)
    
    print('Wins: ' + str(win_count))
    
    print('Losses: ' + str(loss_count))

    
    if loss_count == 0:
        loss_count = 1
        
    print('W/L ratio: ' + str(win_count/loss_count))
    
    sleep_time(on_off, 0.5)
    
    if win_count > loss_count:
        print('You were pretty lucky')
    elif win_count < loss_count:
        print('You were pretty unlucky')


elif money <= 0:

    
    if play_or_not == 'quit':
        print('Smart choice')
        print('Here are your wins and losses and win/loss ratio:')
    
    
    else:       
        print('haha ur too broke to keep playing')
        print("I'll even show ur wins and losses for u")

    sleep_time(on_off, 1)
    
    print('Wins: ' + str(win_count))
    
    print('Losses: ' + str(loss_count))
    if loss_count == 0:
        loss_count = 1
        
    print('W/L ratio: ' + str(win_count/loss_count))
    
    sleep_time(on_off, 0.5)
    
    if win_count > loss_count:
        print('imagine losing even though u were lucky')

        sleep_time(on_off, 0.5)

        print('ur probably just bad at gambling i guess')
        
    elif win_count < loss_count:
        print('haha u were pretty unlucky')

        sleep_time(on_off, 0.5)
        
        print('sucks to suck')















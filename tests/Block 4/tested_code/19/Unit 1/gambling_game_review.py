






    
    
    

    
    
    
    








import random

import time

random.seed()



money = 100


heads_or_tails = 0


play_or_not = 1


loss_count = 0
win_count = 0



print()






def sleep_time(on_off, delay_time):
    if on_off == 1:
        time.sleep(delay_time)
    else:
        time.sleep(0)









on_off = input('Do you want to enable time between outputs(yes/no): ')

if on_off == 'yes':
    on_off = 1
if on_off == 'no':
    on_off = 0

while money > 0 and play_or_not == 1:

    

    random.seed()

    
    amt_bet = 0

    sleep_time(on_off, 0.5)

    print()
    print('you have ' + str(money) + ' dollars right now')
    print()

    sleep_time(on_off, 0.8)
    
    while amt_bet  < 1 or amt_bet > money:
        
        
        amt_bet = int(input('enter how much money you want to bet(you can bet from one up to how much you have): '))
        if amt_bet < 1:
            sleep_time(on_off, 0.5)
            print()
            print('you have to bet more than a dollar')
            print('enter again')
            print()
            
        elif amt_bet > money:
            sleep_time(on_off, 0.5)
            print()
            print('haha ur too broke to bet this much')
            print('enter again')
            print()
    

    
    money -= amt_bet

    sleep_time(on_off, 1)
    
    print()
    player_choice = input('enter your choice (heads/tails): ')
    print()

    
    if player_choice == 'heads':
        player_choice = 1
    elif player_choice == 'tails':
        player_choice = 0
    
    toss_coin = input('do you want do flip the coin(yes/no): ')

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
            
            
            
            amt_bet = amt_bet * 2
            print('You will get ' + str(money + amt_bet) + ' dollars')
            print()
            
            win_count += 1

            sleep_time(on_off, 0.5)
            
            double_or_nothing = input('Do you want to double or nothing?(yes/no): ')

            if double_or_nothing == 'no':
                lose_or_choose = 0
                print('Thats okay, take your money')

                
                money = money + amt_bet

            
            while double_or_nothing == 'yes':

                random.seed()
                
                player_choice = input('enter your choice (heads/tails): ')

                
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
                    amt_bet = amt_bet * 2                   
                    print('You now have ' + str(money + amt_bet) + ' dollars')
                    double_or_nothing = input('double or nothing(yes/no): ')
                    
                    
                    
                    
                    lose_or_choose = 1
                    print()

                    win_count += 1

                
                elif heads_or_tails != player_choice:

                    sleep_time(on_off, 0.7)
                    
                    print('you did not get it')
                    print('you lost ur money')
                    print()
                    print('you now have ' + str(money) + ' dollars')
                    print()
                    
                    
                    lose_or_choose = 0
                    
                    money = money
                    double_or_nothing = 'no'

                    loss_count += 1

            
            
            
            if lose_or_choose != 0:
                money = money + amt_bet
                print("That's okay, take your money")

        
        elif player_choice != heads_or_tails:

            sleep_time(on_off, 0.7)
            
            print('Unfortunately, you did not get it')
            print('you now have ' + str(money) + ' dollars')
            money = money

            loss_count += 1       
    
    elif toss_coin == 'no':

        sleep_time(on_off, 0.5)
        
        print("I'll be taking your money then")
        money = money

    sleep_time(on_off, 0.5)
    
    print()
    
    play_or_not = input('If you want to quit, enter quit, and enter again to play again: ')
    print()
    
    if play_or_not == 'quit':
        play_or_not = 0
    elif play_or_not == 'again':
        play_or_not = 1

sleep_time(on_off, 1)



if money > 0:
    print('Sorry to see you go, all ur money will be wiped :)')
    print('here is your wins and losses and ur win/loss ratio: ')
    
    sleep_time(on_off, 1)
    
    print('Wins: ' + str(win_count))
    
    print('Losses: ' + str(loss_count))

    
    if loss_count == 0:
        loss_count = 1
        
    print('W/L ratio: ' + str(win_count/loss_count))
    
    sleep_time(on_off, 0.5)
    
    if win_count > loss_count:
        print('you were pretty lucky')
    elif win_count < loss_count:
        print('you were pretty unlucky')


elif money <= 0:
    
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















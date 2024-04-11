


import random

import time

display_sym = 0

def time_delay(on_off, length):
    if on_off == 'yes':
        time.sleep(length)
    if on_off == 'no':
        time.sleep(0)



def random_card():
    player_cards = random.randint(1,11)

    display_sym = player_cards

    
    if display_sym == 1:
        display_sym = 'A'
    elif display_sym == 11:
        play_cards = 10
        display_sym = random.randint(1,3)
        if display_sym == 1:
            display_sym = 'Q'
        elif display_sym == 2:
            display_sym = 'K'
        else:
            display_sym = 'J'
    return display_sym




def print_card_image(val_displayed):
    print('''
            ▐▀▀▀▀▀▀▀▀▀▀▌
            ▐          ▌
            ▐          ▌  ''')
    print('            ▐    ' + str(val_displayed) + '    ▐')
    print('''            ▐          ▌
            ▐▄▄▄▄▄▄▄▄▄▄▌
    ''')


on_off = input('Do you want to enable time between outputs(yes/no): ')


print("Let's play blackjack")
opponent_name = input('Enter the name of the person you hate the most: ')
print('You will be playing against ' + opponent_name + ', the dealer')


money = 100

amount_bet = 0

play_or_not = 'yes'


while play_or_not == 'yes':


    time_delay(on_off, 0.5)
    amount_bet = int(input('Enter how much money you want to bet: '))
    time_delay(on_off, 0.5)
    
    while amount_bet < 1 or amount_bet > money:

        time_delay(on_off, 0.7)
        amount_bet = int(input('Enter how much money you want to bet: '))

        time_delay(on_off, 0.7)
        if amount_bet > money:
            print('ur too broke')
            time_delay(on_off, .2)
            print('bet less')

        else:
            print('u have to bet more than 1')
            time_delay(on_off, 0.2)
            print('bet again')


    
    money -= amount_bet

    p_display_card_1 = random_card()
    p_display_card_2 = random_card()

    
    time_delay(on_off, 0.6)
    print('Your cards are: ')
    time_delay(on_off, 0.7)
    print_card_image(p_display_card_1)
    time_delay(on_off, 0.7)
    print('and')
    print_card_image(p_display_card_2)

    
    if p_display_card_1 == 'Q' or p_display_card_1 == 'K' or p_display_card_1 =='J':
        p_display_card_1 = 10

    if p_display_card_2 == 'Q' or p_display_card_2 == 'K' or p_display_card_2 =='J':
        p_display_card_2 = 10

    if p_display_card_1 == 'A':
        p_display_card_1 = 11

    if p_display_card_2 == 'A':
        p_display_card_2 = 11

    player_total = int(p_display_card_1) + int(p_display_card_2)

    
    c_display_card_1 = random_card()
    c_display_card_2 = random_card()

    
    time_delay(on_off, 1)
    print(opponent_name + "'s cards are")
    time_delay(on_off,0.7)
    print_card_image(c_display_card_1)
    time_delay(on_off,0.7)
    print('and')
    print_card_image(c_display_card_2)

    
    if c_display_card_1 == 'Q' or c_display_card_1 == 'K' or c_display_card_1 =='J':
        c_display_card_1 = 10

    if c_display_card_2 == 'Q' or c_display_card_2 == 'K' or c_display_card_2 =='J':
        c_display_card_2 = 10

    if c_display_card_1 == 'A':
        c_display_card_1 = 11

    if c_display_card_2 == 'A':
        c_display_card_2 = 11

    computer_total = int(c_display_card_1) + int(c_display_card_2)

    time_delay(on_off,0.5)
    print('your current total is ' + str(player_total))

    
    tie = 0

    hit_or_stand = 'no'
    
    if player_total == 21:
        
        hit_or_stand = 'no'
        run_hs = 0
        if computer_total == 21:
            time_delay(on_off,0.6)
            print('You both got a blackjack')
            time_delay(on_off,0.2)
            print('You tie')
            
            tie = 1
    else:
        run_hs = 1

    if run_hs == 1:
        time_delay(on_off,0.8)
        hit_or_stand = input('Do you want to hit or stand(yes/no): ')

    
    bust_or_no = 0

    
    p_display_card_1 = 0
    while hit_or_stand == 'yes':
        time_delay(on_off, 0.6)
        print('You got')
        time_delay(on_off, 0.7)
        p_display_card_1 = random_card()
        print_card_image(p_display_card_1)

        if p_display_card_1 == 'Q' or p_display_card_1 == 'K' or p_display_card_1 == 'J':
            p_display_card_1 = 10

        if p_display_card_1 == 'A':
            if player_total + 11 > 21:
                p_display_card_1 = 1
            else:
                p_display_card_1 = 11
        player_total += int(p_display_card_1)
        time_delay(on_off, 0.6)
        print('your new total is ' + str(player_total))
        time_delay(on_off, 0.6)

        if player_total < 21:
            hit_or_stand = input('Do you want to hit or stand(yes/no)')

        elif player_total > 21:
            time_delay(on_off, 0.5)
            print('You went bust')
            hit_or_stand = 'no'
            bust_or_no = 1

        else:
            time_delay(on_off, 0.9)
            print('blackjack!')
            hit_or_stand = 'no'

    c_display_card_1 = 0
    
    while computer_total <= 17 and computer_total != 21:
        time_delay(on_off, 0.6)
        c_display_card_1 = random_card()
        print(opponent_name + ' got')
        print_card_image(c_display_card_1)

        
        if c_display_card_1 == 'Q' or c_display_card_1 == 'K' or c_display_card_1 == 'J':
            c_display_card_1 = 10

        if c_display_card_1 == 'A':
            if computer_total + 11 > 21:
                c_display_card_1 = 1
            else:
                c_display_card_1 = 11

        computer_total += int(c_display_card_1)

    time_delay(on_off, 0.5)
    print(opponent_name + "'s new total is " + str(computer_total))

    
    

    time_delay(on_off,0.9)
    if tie == 0:

        if computer_total > 21 or player_total > 21:
            if bust_or_no == 1 and computer_total > 21:
                print('Both of went bust')
                print('You both lose')
                money += amount_bet

            elif computer_total > 21 and bust_or_no == 0:
                print(opponent_name + ' went bust')
                print('You won')
                money += amount_bet*2
            elif player_total > 21:
                print('You lost')

        elif player_total == 21:
            if computer_total != player_total:
                print('You won')
                money += amount_bet*2
            else:
                print('You both got blackjack')
                print('You tie')
                money += amount_bet

        elif computer_total == 21:
            print(opponent_name + ' got blackjack')
            print('You lose')

        elif bust_or_no == 0:
            if player_total > computer_total:
                print('Your total is greater than ' + opponent_name + "'s")
                print('you won')
                money += amount_bet*2
            elif player_total < computer_total:
                print('Your total is lesser than ' + opponent_name + "'s")
                print('you lost')

    time_delay(on_off, 0.5)
    print('you now have ' + str(money) + ' dollars')

    
    time_delay(on_off, 0.5)

    if money <= 0:
        play_or_not = 'no'
    
    else:
        play_or_not = input('do you want to play again(yes/no)')

time_delay(on_off, 0.7)
print('sad to see you go')
print('play again next time')














from uno_board_functions import *

board = [ ['  ','  '],['  ','  '] ]
card = input('Input your card: ')
judge = 1
list = 0
round = 0

while card != 'quit':

    if ((card[0] == '0' or card[0] == '1' or card[0] == '2' or
          card[0] == '3' or card[0] == '4' or card[0] == '5' or
          card[0] == '6' or card[0] == '7' or card[0] == '8' or
          card[0] == '9' or card[0] == 'S' or card[0] == 'R')
          and (card[1]== 'R' or card[1] == 'B' or card[1] == 'Y' or card[1] == 'G')):

        if round >= 1:
            if check_index[0] != card[0] and check_index[1] != card[1]:
                print('You are the cheater! You are out!')
                break

        make_move(card,board,list,judge)
        draw_board(board)


        
        
        if card[0] == 'R':
            judge += 1
        
        if judge % 2 == 1: 
            if card[0] != 'S':
                
                if list >= 3:
                    list -= 3
                elif list <= 2:
                    list += 1
            elif card[0] == 'S':
                if list >= 2:
                    list -= 2
                elif list <= 1:
                    list += 2
            round += 1
            
        elif judge % 2 == 0: 
            if card[0] != 'S':
                if list <= 0:
                    list += 3
                elif list >= 1:
                    list -= 1
            elif card[0] == 'S':
                if list <= 1:
                    list += 2
                elif list >= 2:
                    list -= 2
            round += 1

            
        check_index = card 

    else:
        print('Your input is invalid')

    card = input('Input your card: ')
   

if card == 'quit':
    print()
    print('See you next time')



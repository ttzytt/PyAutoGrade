




from tic_tac_toe_functions_part_1 import *



board = [ [' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' '] ]
player = 'x'
draw_board(board)
play_time = 0

print()
move = input('X player, choose your first move: ')
print()




while find_winner(board) == None and is_full(board,play_time) == False:
    

    if move == 'quit':
        print('See you next time')
        break
        
    
    if make_move(player,move,board) == True:
        

        play_time += 1 
        make_move(player,move,board) 
        draw_board(board) 
        player = next_player(player) 
        
        if find_winner(board) == None and is_full(board,play_time) == False:
            
            
            
            print()
            if player == 'o':
                move = input('O player, choose your move: ')
            elif player == 'x':
                move = input('X player, choose your move: ')
            print()
            
    elif make_move(player,move,board) == False:
        
        
        print()
        print('You made an invalid movement')
        print()
        move = input('Choose your move again: ')



if find_winner(board) != None: 
    print()
    if find_winner(board) == 'x':
        print('The X player wins!')
    elif find_winner(board) == 'o':
        print('The O player wins!')




if is_full(board,play_time) == True: 
    print()
    print('Nobody wins, we tie')



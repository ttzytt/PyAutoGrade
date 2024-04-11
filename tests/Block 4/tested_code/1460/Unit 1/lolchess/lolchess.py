from lolchess_class import *    

'''
!!! SETUP !!!
'''


white = Player('W')
black = Player('B')


store = Store(pieces, 5)
store.setup()

shed = Shed(pieces, 5)
shed.setup()

white.vip_store = VIPStore(white, pieces)
black.vip_store = VIPStore(black, pieces)

white.church = Church(white)
black.church = Church(black)


board = Board(13, 7, [white, black], pieces)
board.setup_bitboards(pieces)


nexus = pieces[0]
nexus_guard = pieces[1]
board.set_piece(white, nexus, [1, 13])
board.set_piece(white, nexus_guard, [2, 13])
board.set_piece(white, nexus_guard, [2, 12])
board.set_piece(white, nexus_guard, [1, 12])

board.set_piece(black, nexus, [7, 1])
board.set_piece(black, nexus_guard, [6, 2])
board.set_piece(black, nexus_guard, [7, 2])
board.set_piece(black, nexus_guard, [6, 1])

'''
!!! INSTRUCTIONS !!!
'''

instructions_string = '''
Welcome to LOLChess. 

LOLChess is similar to chess. It's played on a 7 x 13 board, and
has a wide assortment of pieces.

The goal of this game is to capture the opposing player's Nexus,
which looks like this: ⛋.

This Nexus, along with every other piece in this game, has a
few properties:
    Name and Info - What is this piece?
    Movement Pattern - How this piece moves.
    Attack Pattern - How this piece attacks.
    Cost - How much does this piece cost to mount.
    Rarity - How rare is the piece.

For example:
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐
│ ╔═══╗ [      Rookie       ] │
│ ║ ♖ ║       UNCOMMON        │
│ ╚ ═ ╝ Cost:  5 ✧            │
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘

" An aspriring rook. "


Attack Pattern:
╔═════╦═════╦═════╦═════╦═════╗
║     ║     ║ ▓▓▓ ║     ║     ║
║     ║     ║ ▓▓▓ ║     ║     ║
╠═════╬═════╬═════╬═════╬═════╣
║     ║     ║ ▓▓▓ ║     ║     ║
║     ║     ║ ▓▓▓ ║     ║     ║
╠═════╬═════╬═════╬═════╬═════╣
║ ▓▓▓ ║ ▓▓▓ ║ /// ║ ▓▓▓ ║ ▓▓▓ ║
║ ▓▓▓ ║ ▓▓▓ ║ /// ║ ▓▓▓ ║ ▓▓▓ ║
╠═════╬═════╬═════╬═════╬═════╣
║     ║     ║ ▓▓▓ ║     ║     ║
║     ║     ║ ▓▓▓ ║     ║     ║
╠═════╬═════╬═════╬═════╬═════╣
║     ║     ║ ▓▓▓ ║     ║     ║
║     ║     ║ ▓▓▓ ║     ║     ║
╚═════╩═════╩═════╩═════╩═════╝

Movement Pattern:
╔═════╦═════╦═════╦═════╦═════╦═════╦═════╗
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣
║ ▓▓▓ ║ ▓▓▓ ║ ▓▓▓ ║ /// ║ ▓▓▓ ║ ▓▓▓ ║ ▓▓▓ ║
║ ▓▓▓ ║ ▓▓▓ ║ ▓▓▓ ║ /// ║ ▓▓▓ ║ ▓▓▓ ║ ▓▓▓ ║
╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
╠═════╬═════╬═════╬═════╬═════╬═════╬═════╣
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
║     ║     ║     ║ ▓▓▓ ║     ║     ║     ║
╚═════╩═════╩═════╩═════╩═════╩═════╩═════╝

You can view the above properties of any piece at any time
by typing '/lookup {piece 1} {piece 2} {...}'. To view a list of all the pieces,
type '/index'.
    

Each turn consists of 4 phases:
    1. Mounting Phase - Place your pieces :)
    2. Movement Phase - Move your pieces :)
    3. Opponent Movement Phase - Your opponent moves some pieces :(
    4. Attacking Phase - Attack some pieces :)

Mounting Phase:

Pieces can be bought through the Store, which randomly selects
5 pieces to go on sale. This Shop is shared between both players,
so if one person buys a piece, the other can no longer obtain it.
There is additionally a VIP store, which you can unlock through
the Church (explained later).

LOLChess’s currency will be $, which can be earned through the
following methods:
    • Each player starts with 10$.
    • Every turn, earn 3$.
    • For every COMMON and UNCOMMON capture, earn 3$.
    • For every RARE, LEGENDARY, and SPECIAL capture, earn 5$.
    • For every Nexus Guard broken, earn 7$.
However, during the first three turns turn, only Starting Pieces
can be bought and placed. This will use a specialized shop: The Shed.

Finally, a shop with upgrades exists: The Church.
Each player gets their own church, with the same, permanently
available upgrades. 
These upgrades are aimed to be purchased during the late-game due
to their low price-to-value ratio and high opportunity cost, and are:
    1. VIP customer - (5$) (Max: 3): Increases the Shop’s slots by 1
        for you. The extra pieces in this area are different for each
        player, and stock is not shared.
        
    2. On Guard - (7$) (Max: None): Increases the number of pieces you
        can move after your opponent moves. 
        You can only move at most the same number of pieces your
        opponent does, and any excess of this upgrade will not take
        effect for this round (base: 3).
        
    3. Feisty - (8$) (Max: 2): Increases the number of pieces you can
        select to attack with (base: 3).
    
After buying your pieces and upgrades, you can place your bought pieces 
in the first 3 rows of your side.
      
Movement Phase:
This phase is pretty simple. Move your pieces according to their movement 
patterns. 
However, remember that you cannot immediately attack after: the opponent 
gets a turn to move a base of 2 pieces, which can be upgraded to up to 5.

Opposing Movement Phase:
Your opponent gets to move!!! Right before you were about to attack... Drats.
They're allowed to move a base of 2 pieces but this can be increased thourgh 
the Church.

Attacking Phase:
Select the pieces you want to attack with, up to 1. This max-attack limit 
can be upgraded via the Church. 
Pieces CAN attack through other pieces, so be careful, and use your
counter-movement phases wisely.
      
Now that you've gotten the jist of it, we have one last message:
                  ╔══════════════════════╗
                  ║ Welcome to LOLChess. ║
                  ╚══════════════════════╝
'''






instructions_buffer = 10
instructions_lines = instructions_string.split('\n')
instructions_lines = list(map(lambda x: x.strip(), instructions_lines)) 

instructions_page = 1
instructions_page_length = 15


while instructions_page < len(instructions_lines) // instructions_page_length + 1: 
    for line in instructions_lines[ : instructions_page * instructions_page_length]:
        print(instructions_buffer * ' ', '|', line)
    print('Press Enter to continue.')
    input()
    instructions_page += 1
    wash_screen()


'''
!!! GAMEPLAY LOOP !!!
'''

active_player = board.players[-1]
flipped = True
culmutive_turn = 1
turns_till_store = 3 
while not board.get_is_game_ended():
    
    
    active_player = board.players[(board.players.index(active_player) + 1) % len(board.players)]
    culmutive_turn += 1
    turn = culmutive_turn // len(board.players)
    flipped = not flipped

    
    if turn % 3 == 0:
        store.reset()
        active_player.vip_store.reset()
    
    
    
    

    

    
    shop_options = []
    if turn <= turns_till_store:
        shop_options.append("The Shed")
    else:
        shop_options.append("The Store")
    if active_player.vip_store.slots > 0:
        shop_options.append("VIP Store")
    shop_options.append('The Church')
    is_buying = True
    pieces_bought = []

    
    
    def buy_process(store):
        print()
        store.print_store()
        print()
        player_input = game_input("Please write the # of the item you would like to buy:",
                                  "(just press ENTER if nothing.) ")
        has_completed_buying = False
        if player_input == '':
            has_completed_buying = True
        while not has_completed_buying:     
            
            if '1' <= player_input <= str(len(store.offers)) and len(player_input) == 1:
                buy_response = store.buy(active_player,int(player_input))
                if buy_response is not False: 
                    pieces_bought.append(buy_response)
                    store.print_store()
            else:
                game_print("Please provide a valid input.")
            player_input = game_input("Please write the # of the item you would like to buy:",
                                      "(just press ENTER if nothing) ")
            if player_input == '':
                has_completed_buying = True
        wash_screen()
        return True
    
    
    
    def church_buy_process():
        church = active_player.church
        church.print_shop()
        player_input = game_input("Please write the # of the upgrade you would like to",
                                  "upgrade: (just press ENTER if nothing.) ")
        has_completed_buying = False
        if player_input == '':
            has_completed_buying = True
        while not has_completed_buying:     
            
            
            if '1' <= player_input <= str(len(church.offers)) and len(player_input) == 1:
                church.upgrade_level(int(player_input))
            else:
                game_print("Please provide a valid input.")
            player_input = game_input("Please write the # of the item you would like to buy:",
                                      "(just press ENTER if nothing) ")
            if player_input == '':
                has_completed_buying = True
        
        VIP_store_level = active_player.upgrades[list(map(lambda x: x['upgrade'], active_player.upgrades)).index('shop_increase')]['level']
        if active_player.vip_store.slots < VIP_store_level:
            for _ in range(active_player.upgrades[0]['level'] - active_player.vip_store.slots):
                active_player.vip_store.increase_slots()
        wash_screen()
        return True


    
    print(f"TURN {turn} - PLAYER {board.players.index(active_player) + 1}'s TURN //",
          f"BALANCE: {active_player.balance}$ // PIECES IN CART:",', '.join(list(map(lambda x: x.name,pieces_bought))))

    player_input = game_input(f"Where would you like to go: ({', '.join(shop_options)}, The Exit) ").lower()
    if player_input == 'the exit':
        is_buying = False
    else:
        while player_input not in list(map(lambda x: x.lower(), shop_options)) and player_input != 'the exit': 
            game_print("That's not a valid place!")
            print(f"TURN {turn} - PLAYER {board.players.index(active_player) + 1}'s TURN //",
                  "BALANCE: {active_player.balance}$ // PIECES IN CART:",
                  {', '.join(list(map(lambda x: x.name,pieces_bought)))})
            player_input = game_input(f"Where would you like to go: ({', '.join(shop_options)}, The Exit) ").lower()
            if player_input == 'the exit':
                is_buying = False
        
    while is_buying:
        wash_screen()
        if player_input == 'the shed':
            buy_process(shed)
        elif player_input == 'the store':
            buy_process(store)
        elif player_input == 'vip store':
            buy_process(active_player.vip_store)
        elif player_input == 'the church':
            church_buy_process()

        if active_player.vip_store.slots > 0 and 'vip store' not in shop_options:
            shop_options.append('VIP Store')
        print(f"TURN {turn} - PLAYER {board.players.index(active_player) + 1}'s TURN //"
              ,"BALANCE: {active_player.balance}$ // PIECES IN CART:",
              {', '.join(list(map(lambda x: x.name,pieces_bought)))})
        player_input = game_input(f"Where would you like to go: ({', '.join(shop_options)}, The Exit) ").lower()
        if player_input == 'the exit':
            is_buying = False
            wash_screen()
        else:
            while player_input not in list(map(lambda x: x.lower(), shop_options)) and player_input != 'the exit':
                game_print("That's not a valid place!")
                print(f"TURN {turn} - PLAYER {board.players.index(active_player) + 1}'s TURN // BALANCE: {active_player.balance}$ // PIECES IN CART: {', '.join(list(map(lambda x: x.name,pieces_bought)))}")
                player_input = game_input("Where would you like to go:"
                                          f"({', '.join(shop_options)}, The Exit) ").lower()
                if player_input == 'the exit':
                    is_buying = False

    
    for piece in pieces_bought:
        avaliable_mounting_squares = []

        
        
        if flipped: 
            y_range = range(1,4)
        else:
            y_range = range(board.height - 2, board.height+1)

        for x in range(1,board.width+1):
            for y in y_range:
                if board.get_piece_at_square([x, y]) == (None, None):
                    avaliable_mounting_squares.append([x,y])
                    
        board.print_board(flipped, 10, avaliable_mounting_squares)

        
        if len(avaliable_mounting_squares) == 0:
            game_print("Well, I guess everywhere's full...")
            game_print("Here's a refund for:", piece.name)
            active_player.balance += piece.mounting_details['cost']
            active_player.pieces.pop(-1)
        else:
            target_square = get_coordinate_from_player(board, f"Choose a location to place your {piece.name}",
                                                       avaliable_mounting_squares, "That's not an avaliable square.")
            board.set_piece(active_player, piece, target_square)

    
    game_print("MOVEMENT PHASE")
    highlighted_squares = []
    for x in range(1, board.width + 1):
        for y in range(1, board.height + 1):
            square_player, square_piece = board.get_piece_at_square([x, y])
            if square_player is active_player:
                highlighted_squares.append([x,y])
    

    board.print_board(flipped, 10, highlighted_squares=highlighted_squares)
    is_movement_phase = True

    target_square = get_coordinate_from_player(board, "Type the coordinate of the piece you want to move. (Highlighted are potentially avaliable; 'end' to end phase.) ",
                                               highlighted_squares, "You can't move that piece!", 'end')
    while target_square is False:
        target_square = get_coordinate_from_player(board, "Type the coordinate of the piece you want to move. (Highlighted are potentially avaliable; 'end' to end phase.) ",
                                                   highlighted_squares, "You can't move that piece!", 'end')

    if target_square is True:
        is_movement_phase = False

    while is_movement_phase:
        selected_piece = board.get_piece_at_square(target_square)[1]
        
        possible_movement_squares = []
        pattern = selected_piece.movement_pattern['pattern']
        if flipped:
            pattern = list(reversed(pattern))
        piece_position = selected_piece.movement_pattern['piece_position']
        for row in range(len(pattern)):
            for column in range(len(pattern)):
                
                if pattern[row] & 1 << (len(pattern) - column - 1) != 0:
                    potential_x = target_square[0] + column - piece_position[0]
                    potential_y = target_square[1] + row - piece_position[1]
                    
                    if 1 <= potential_x <= board.width and 1 <= potential_y <= board.height and board.get_piece_at_square([potential_x, potential_y]) == (None, None):
                        possible_movement_squares.append([potential_x,potential_y])
        board.account_for_blocking(target_square, possible_movement_squares, active_player)
        board.print_board(flipped, 10, highlighted_squares=possible_movement_squares)
        movement_target_square = get_coordinate_from_player(board, "Type the coordinate of where you want to move to. (Highlighted are avaliable; type 'exit' to exit.) ",
                                                            possible_movement_squares, "You can't move there!", 'exit')
        if movement_target_square is not False and movement_target_square is not True:
            
            board.clear_square(target_square)
            
            highlighted_squares.remove(target_square)
            
            board.print_bitboards()
            
            board.set_piece(active_player, selected_piece, movement_target_square)

        board.print_board(flipped, 10, highlighted_squares=highlighted_squares)
        target_square = get_coordinate_from_player(board, "Type the coordinate of the piece you want to move. (Highlighted are avaliable; 'end' to end phase.) ",
                                                   highlighted_squares, "You can't move that piece!", 'end')
        if target_square is True:
            is_movement_phase = False

    
    game_print("OPPONENT'S MOVEMENT PHASE:")
    
    flipped = not flipped
    
    highlighted_squares = []
    for x in range(1, board.width + 1):
        for y in range(1, board.height + 1):
            square_player, square_piece = board.get_piece_at_square([x, y])
            if square_player is board.players[(board.players.index(active_player) + 1) % len(board.players)]:
                highlighted_squares.append([x,y])
    

    board.print_board(flipped, 10, highlighted_squares=highlighted_squares)
    is_movement_phase = True
    pieces_moved = 0
    number_of_movable_pieces = 2 + active_player.upgrades[list(map(lambda x: x['upgrade'], active_player.upgrades)).index('counter_attack_increase')]['level']
    game_print(f"You have {number_of_movable_pieces - pieces_moved} moves left.")
    target_square = get_coordinate_from_player(board, "Type the coordinate of the piece you want to move. (Highlighted are avaliable; 'end' to end phase.) ",
                                               highlighted_squares, "You can't move that piece!", 'end')
    if target_square is True:
        is_movement_phase = False

    while is_movement_phase:
        selected_piece = board.get_piece_at_square(target_square)[1]
        
        possible_movement_squares = []
        pattern = selected_piece.movement_pattern['pattern']
        if flipped:
            pattern = list(reversed(pattern))
        piece_position = selected_piece.movement_pattern['piece_position']
        for row in range(len(pattern)):
            for column in range(len(pattern)):
                
                if pattern[row] & 1 << (len(pattern) - column - 1) != 0:
                    potential_x = target_square[0] + column - piece_position[0] 
                    potential_y = target_square[1] + row - piece_position[1]
                    
                    if 1 <= potential_x <= board.width and 1 <= potential_y <= board.height and board.get_piece_at_square([potential_x, potential_y]) == (None, None):
                        possible_movement_squares.append([potential_x,potential_y])

        board.account_for_blocking(target_square, possible_movement_squares, active_player)

        board.print_board(flipped, 10, highlighted_squares=possible_movement_squares)
        movement_target_square = get_coordinate_from_player(board, "Type the coordinate of where you want to move to. (Highlighted are avaliable; type 'exit' to exit.) ",
                                                            possible_movement_squares, "You can't move there!", 'exit')
        


        if movement_target_square is not False and movement_target_square is not True:
            
            highlighted_squares.remove(target_square)
            board.set_piece(board.players[(board.players.index(active_player) + 1) % len(board.players)], selected_piece, movement_target_square)
            board.clear_square(target_square)
            pieces_moved += 1

        board.print_board(flipped, 10, highlighted_squares=highlighted_squares)
        game_print(f"You have {number_of_movable_pieces - pieces_moved} moves left.")
        if number_of_movable_pieces - pieces_moved > 0:
            target_square = get_coordinate_from_player(board, "Type the coordinate of the piece you want to move. (Highlighted are avaliable; 'end' to end phase.) ",
                                                       highlighted_squares, "You can't move that piece!", 'end')
            if target_square is True:
                is_movement_phase = False
        else:
            is_movement_phase = False
    flipped = not flipped

    
    game_print("ATTACKING PHASE")
    highlighted_squares = []
    
    for x in range(1, board.width + 1):
        for y in range(1, board.height + 1):
            square_player, square_piece = board.get_piece_at_square([x, y])
            
            if square_player is active_player:
                has_attack = False
                for row in square_piece.attack_pattern['pattern']:
                    if row != 0:
                        has_attack = True
                if has_attack:
                    highlighted_squares.append([x,y])
    pieces_attacked = 0
    
    number_of_attacking_pieces = 1 + active_player.upgrades[list(map(lambda x: x['upgrade'], active_player.upgrades)).index('attack_increase')]['level']
    is_attack_phase = True
    board.print_board(flipped, 10, highlighted_squares=highlighted_squares)
    game_print(f"You have {number_of_attacking_pieces - pieces_attacked} moves left.")
    target_square = get_coordinate_from_player(board, "Type the coordinate of the piece you want to attack with. (Highlighted are avaliable; 'end' to end phase.) ",
                                               highlighted_squares, "You can't attack with that piece!", 'end')
    if target_square is True:
        is_attack_phase = False
    if target_square is False:
        wash_screen()
        game_print("No valid squares to use.")
        is_attack_phase = False

    while is_attack_phase:
        selected_piece = board.get_piece_at_square(target_square)[1]
        
        possible_attack_squares = []
        pattern = selected_piece.attack_pattern['pattern']
        if flipped: 
            pattern = list(reversed(pattern))
        piece_position = selected_piece.attack_pattern['piece_position']
        for row in range(len(pattern)):
            for column in range(len(pattern)):
                
                if pattern[row] & 1 << (len(pattern) - column - 1) != 0:
                    potential_x = target_square[0] + column - piece_position[0]
                    potential_y = target_square[1] + row - piece_position[1]
                    if 1 <= potential_x <= board.width and 1 <= potential_y <= board.height:
                        possible_attack_squares.append([potential_x,potential_y])
        
        
        board.account_for_blocking(target_square, possible_attack_squares, active_player)

        print(possible_attack_squares)
        board.print_board(flipped, 10, highlighted_squares=possible_attack_squares)
        player_input = input("Are you sure you want to attack with this square? (Y/N) ").lower()
        if player_input in ['y', 'yes']:
            
            highlighted_squares.remove(target_square)
            for square in possible_attack_squares:
                if board.get_piece_at_square(square)[1] is not None:
                    board.get_piece_at_square(square)[1].gets_captured(active_player, selected_piece, target_square, square, board)
                    board.clear_square(square)
            pieces_attacked += 1
            if board.get_is_game_ended():
                break
        
        if board.get_is_game_ended():
                break
        
        board.print_board(flipped, 10, highlighted_squares=highlighted_squares)
        game_print(f"You have {number_of_attacking_pieces - pieces_attacked} moves left.")
        if number_of_attacking_pieces - pieces_attacked > 0:
            target_square = get_coordinate_from_player(board, "Type the coordinate of the piece you want to attack with. (Highlighted are avaliable; 'end' to end phase.) ",
                                                       highlighted_squares, "You can't attack with that piece!", 'end')
            if target_square is False:
                game_print("No valid squares to use.")
                is_attack_phase = False
            if target_square is True:
                is_attack_phase = False
        else:
            is_attack_phase = False
    if board.get_is_game_ended():
        break
    active_player.balance += 3


game_print("GG")




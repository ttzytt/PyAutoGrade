"""
The following functions and classes are for use in making a variant
of Chess.

For all of the code below, the board will be a 7 by 13 grid, with
the bottom left corner being (1, 13) and the top right corner being
(7, 1).  The board's pieces will be stored in a dictionary that
contains the bitboards of each piece. For example, a White Knight
will be stored in 'W_Knight' and a Black Pawn will be stored in
'B_Pawn'. The bitboard will be a 91-bit integer, with the 
leftmost bit being the top left corner and the rightmost bit
being the bottom right corner.

For example, in a game with a White Knight on (1, 1) and no
other pieces, the dictionary bitboards will have the following
values:

W_Knight: 0b1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
B_Knight: 0b0
W_Pawn: 0b0
B_Pawn: 0b0
...

Squares and coordinates are inputted as a list of two integers,
[x, y], with the bottom left corner being [1, 13] and the top
right corner being [7, 1]. In certain functions, the coordinates
can be inputted as a single integer, with the number 1 corresponding
to the top left and the number 91 corresponding to the bottom right.

Moves are inputted as strings that contain a number and a letter.

Players are the active players in the game, being differentiated by color.
They each have their own VIP shops and Churches, which are player-specific
shops in the game.
"""

import random




has_ended = False




COMMON = 1
UNCOMMON = 0.75
RARE = 0.5
LEGENDARY = 0.15
SPECIAL = 0.25




color_symbols = {'W': '●', 'B': '○'}







class Gimmick:
    '''
    Inputs
        name - The Gimmick name
        description - The Gimmick's description

    
    
    '''
    def __init__(self, name, description, type, function, value = None, value_modifier = None):
        self.name = name
        self.description = description
        self.type = type
        self.function = function
        self.value = value
        self.value_modifier = value_modifier

    # value_change should be lambda
    def activate(self, player, piece, start_coords, end_coords, board):
        if self.value is not None and self.value_modifier is not None:
            self.value = self.value_modifier(self.value)
            self.function(player, piece, start_coords, end_coords, board, self.value)
        elif self.value is not None:
            self.function(player, piece, start_coords, end_coords, board, self.value)
        else:
            self.function(player, piece, start_coords, end_coords, board)
        

class Piece:
    '''
    Inputs:
        name - The piece's name.
        symbol - The piece's symbol on the board.
        description - The piece's description for the piece encyclopedia.
        movement_pattern - The piece's movement pattern.
        attack_pattern - The piece's attack pattern.
        mounting_details - The piece's mounting requirements.
        gimmick_functions - An object containing the functions that need to be run during
                            each function.
        rarity - The rarity of the piece (changes shop chances)
    '''
    def __init__(self, 
                 name, symbol,
                 description = None,
                 movement_pattern = {'pattern': [0], 'piece_position': [0,0]},
                 attack_pattern = {'pattern': [0], 'piece_position': [0,0]},
                 mounting_details = {'starting': True, 'cost': 3, 'unbuyable': False},
                 gimmick_functions = {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
                 rarity = COMMON
                 ):
        self.name = name
        self.symbol = symbol
        self.description = description
        self.movement_pattern = movement_pattern
        self.attack_pattern = attack_pattern
        self.mounting_details = mounting_details
        self.gimmick_functions = gimmick_functions
        self.rarity = rarity

    # Inputs:
    #   player - Player who owns the captured piece. [Type: Player]
    #   piece - The type of piece. [Type: Piece]
    #   start_coords - The coordinates of the piece that captured the piece. [Type: int or list]
    #   end_coords - The coordinates of the piece that got captured. [Type: int or list]
    def gets_captured(self, player, piece, start_coords, end_coords, board):
        # If the coordinates are in [x, y] form, change them to integer.
        if not type(start_coords) == int:
            start_coords = start_coords[0] + (start_coords[1] - 1) * board.width
        if not type(end_coords) == int:
            end_coords = end_coords[0] + (end_coords[1] - 1) * board.width
        if piece.rarity in [COMMON, UNCOMMON]:
            board.players[(board.players.index(player)) % len(board.players)].balance += 3
        elif piece.rarity in [RARE, LEGENDARY, SPECIAL]:
            board.players[(board.players.index(player)) % len(board.players)].balance += 5
        for gimmick in self.gimmick_functions['on_capture']:
            gimmick.activate(player, piece, start_coords, end_coords, board)

    # Prints the pattern.
    def print_pattern(self, pattern_type):
        number_of_rows = len(pattern_type['pattern'])
        grid_array = []
        # First Line:
        first_line = ['╔']
        for i in range(number_of_rows-1):
            first_line.append('╦')
        first_line.append('╗')
        grid_array.append('═════'.join(first_line))

        for row in range(number_of_rows):
            # Each Row
            for i in range(2):
                row_array = ['║']
                for column in range(number_of_rows):
                    row_array.append(' ')
                    if pattern_type['piece_position'] == [column,row]:
                        row_array.append('///')
                    elif (pattern_type['pattern'][row] & 1 << (number_of_rows - column - 1)):
                        row_array.append('▓▓▓')
                    else:
                        row_array.append('   ')
                    row_array.append(' ║')
                grid_array.append(''.join(row_array))
            # Edge
            row_array = ['╠']
            for i in range(number_of_rows-1):
                row_array.append('╬')
            row_array.append('╣')
            grid_array.append('═════'.join(row_array))

        # Remove Last Line
        grid_array.pop()
        # New Last Line
        last_line = ['╚']
        for i in range(number_of_rows-1):
            last_line.append('╩')
        last_line.append('╝')
        grid_array.append('═════'.join(last_line))
        print('\n'.join(grid_array))

    '''
    ▛▮▜
    ▙♗▟  ▯
    '''

    # Assumes movement pattern is square
    def print_movement_pattern(self):
        # Error checking for me :)
        if self.movement_pattern['piece_position'][0] >= len(self.movement_pattern['pattern']) or \
            self.movement_pattern['piece_position'][1] >= len(self.movement_pattern['pattern']) or \
            self.movement_pattern['piece_position'][0] < 0 or self.movement_pattern['piece_position'][1] < 0:
            print("Piece position out of bounds.")
            return False
        for row in self.movement_pattern['pattern']:
            if row > (1 << len(self.movement_pattern['pattern'])):
                print("Pattern too wide. Consider adding rows to the bottom.")
                return False
        self.print_pattern(self.movement_pattern)
        return True

    def print_attack_pattern(self):
        # Error checking for me :)
        if self.attack_pattern['piece_position'][0] >= len(self.attack_pattern['pattern']) or \
            self.attack_pattern['piece_position'][1] >= len(self.attack_pattern['pattern']) or \
            self.attack_pattern['piece_position'][0] < 0 or self.attack_pattern['piece_position'][1] < 0:
            print("Piece position out of bounds.")
            return False
        for row in self.attack_pattern['pattern']:
            if row > (1 << len(self.attack_pattern['pattern'])):
                print("Pattern too wide. Consider adding rows to the bottom.")
                return False
        self.print_pattern(self.attack_pattern)
        return True

    def print_business_card(self):
        starting_string = ''
        if self.mounting_details['starting']:
            starting_string = '✧'
        # Sets the string to be printed depending on a piece's rarity.
        rarity_string = ''
        if self.rarity == COMMON:
            rarity_string = 'COMMON'
        elif self.rarity == UNCOMMON:
            rarity_string = 'UNCOMMON'
        elif self.rarity == RARE:
            rarity_string = 'RARE'
        elif self.rarity == LEGENDARY:
            rarity_string = 'LEGENDARY'
        elif self.rarity == SPECIAL:
            rarity_string = 'SPEICAL'
        elif self.rarity == None:
            rarity_strying = 'PRICELESS'
        print(
f'''
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐
│ ╔═══╗ [{self.name:^19}] │
│ ║ {self.symbol} ║{rarity_string:^23}│
│ ╚ ═ ╝ Cost: {self.mounting_details['cost']:>2} {starting_string}            │
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
'''
              )
        print('"', self.description, '"')
        print()
        print("Attack Pattern:")
        self.print_attack_pattern()
        print()
        print("Movement Pattern:")
        self.print_movement_pattern()

        print()
        has_movement_gimmicks = len(self.gimmick_functions['movement']) > 0
        has_attack_gimmicks = len(self.gimmick_functions['attack']) > 0
        has_mounting_gimmicks = len(self.gimmick_functions['mounting']) > 0
        has_on_capture_gimmicks = len(self.gimmick_functions['on_capture']) > 0
        if has_movement_gimmicks:
            print("Movement Gimmicks:")
            for gimmick in self.gimmick_functions['movement']:
                print(f"{gimmick.name} - {gimmick.description}")
            print()
        if has_attack_gimmicks:
            print("Attack Gimmicks:")
            for gimmick in self.gimmick_functions['attack']:
                print(f"{gimmick.name} - {gimmick.description}")
            print()
        if has_mounting_gimmicks:
            print("Mounting Gimmicks:")
            for gimmick in self.gimmick_functions['mounting']:
                print(f"{gimmick.name} - {gimmick.description}")
            print()
        if has_on_capture_gimmicks:
            print("On Capture Gimmicks:")
            for gimmick in self.gimmick_functions['on_capture']:
                print(f"{gimmick.name} - {gimmick.description}")
            print()


class Player:
    def __init__(self,
                 color,
                 pieces = [],
                 balance = 10,
                 upgrades = [{'upgrade': 'shop_increase', 'level': 0, 'max': 3, 'cost': 5, 'display_name': 'VIP Customer', 
                              'description': '    Unlocks and increases the number of offers in the VIP Shop.'},
                             {'upgrade': 'counter_attack_increase', 'level': 0, 'max': 0, 'cost': 7, 'display_name': 'On Guard', 
                              'description': '''    Increases the number of pieces you can move after your opponent moves. 
    You can only move at most the same number of pieces your opponent does,
    and any excess levels for this upgrade will not take effect for this round.'''},
                             {'upgrade': 'attack_increase', 'level': 0, 'max': 2, 'cost': 8, 'display_name': 'Fiesty', 
                              'description': '    Increases the number of pieces you can select to attack with.'}]):
        self.color = color
        self.pieces = pieces
        self.balance = balance
        self.upgrades = upgrades
        
        self.vip_store = None
        self.church = None

    def print_details(self):
        print(f'''
COLOR: {self.color}
PIECES: {self.pieces}
BALANCE: {self.balance}
UPGRADES: {self.upgrades[0]['level']}
              ''')



class Store:
    def __init__(self, avaliable_pieces, slots, offers = []):
        self.avaliable_pieces = []
        for piece in avaliable_pieces:
            if not piece.mounting_details['unbuyable']:
                self.avaliable_pieces.append(piece)
        self.slots = slots
        self.offers = offers

    
    
    def setup(self):
        open_slots = self.slots - len(self.offers)
        self.offers += random.choices(self.avaliable_pieces, weights=list(map(lambda x: x.rarity, self.avaliable_pieces)), k=open_slots)
        return self.offers
    
    
    
    def reset(self):
        open_slots = self.slots
        self.offers = []
        self.offers += random.choices(self.avaliable_pieces, weights=list(map(lambda x: x.rarity, self.avaliable_pieces)), k=open_slots)
        return self.offers

    
    def print_store(self):
        for i,offer in enumerate(self.offers):
            name = 'SOLD OUT'
            cost = '∞'
            if offer is not None:
                name = offer.name
                cost = offer.mounting_details["cost"]
            print(f'[{i+1}] - {name:<30} | Cost: {cost}')
        return

        
    
    
    
    
    
    
    def buy(self, player, item_index):
        target_item = self.offers[item_index-1]
        if target_item is None:
            print("That's sold out...")
            return False
        target_item_price = target_item.mounting_details['cost']
        
        if player.balance < target_item_price:
            print("You're too poor :9(")
            return False
        
        confirmation = input(f"Are you sure you want to buy: {target_item.name} for {target_item_price}? (Y/N) ").lower()
        if confirmation not in ['y', 'yes']:
            print("Ok...")
            return False
        
        player.balance -= target_item_price
        player.pieces.append(target_item)
        self.offers[item_index-1] = None
        print("Thank you for your purchase :)")
        return target_item

class Shed(Store):
    def __init__(self, avaliable_pieces, slots, offers = []):

        self.slots = slots
        self.offers = offers

        
        self.avaliable_pieces = []
        for piece in avaliable_pieces:
            if piece.mounting_details['starting']:
                self.avaliable_pieces.append(piece)  

class VIPStore(Store):
    def __init__(self, player, avaliable_pieces, slots = 0, offers = []):
        self.player = player
        self.slots = slots
        self.offers = offers

        self.avaliable_pieces = []
        
        for piece in avaliable_pieces:
            if piece.rarity in [RARE, LEGENDARY, SPECIAL]:
                self.avaliable_pieces.append(piece)


    def increase_slots(self):  
        
        
        
        
        
        def balance_rarities(piece):
            if piece.rarity == LEGENDARY:
                return 0.2
            else:
                return 0.3  

        
        if self.slots >= 3:
            print("how did you increase slots past the max what...")
            return False
        
        self.slots += 1
        self.offers += random.choices(self.avaliable_pieces, weights=list(map(balance_rarities, self.avaliable_pieces)), k=1)

    def reset(self):
        
        
        
        
        
        
        def balance_rarities(piece):
            if piece.rarity == LEGENDARY:
                return 0.2
            elif piece.rarity == RARE:
                return 0.4
            else:
                return 0.3
        open_slots = self.slots
        self.offers = []
        self.offers += random.choices(self.avaliable_pieces, weights=list(map(balance_rarities, self.avaliable_pieces)), k=open_slots)
        return self.offers
    
class Church():
    def __init__(self, player):
        self.player = player
        self.offers = player.upgrades

    def print_shop(self):
        for i, upgrade in enumerate(self.offers):
            max_level = upgrade['max']
            if max_level == 0:
                max_level = '∞'
            print(f"[{i+1}] - {upgrade['display_name']} - Level {upgrade['level']}/{max_level} \n{upgrade['description']}")

    def upgrade_level(self, upgrade_id):
        
        if type(upgrade_id) == int:
            target_upgrade = self.offers[upgrade_id-1]
            target_upgrade_index = upgrade_id-1
        else:
            
            target_upgrade = None
            for i, upgrade in enumerate(self.offers):
                if upgrade['upgrade'] == upgrade_id:
                    target_upgrade = upgrade
                    target_upgrade_index = i
            if target_upgrade is None:
                print("Invalid Upgrade ID")
                return False
        
        if self.player.balance < target_upgrade['cost']:
            print("Too poor haha")
            return False
        
        if target_upgrade['level'] == target_upgrade['max']:
            print("Cannot upgrade any further!")
            return False
        
        confirmation = input(
            f"Are you sure you want to upgrade: {target_upgrade['display_name']} from Level {target_upgrade['level']} to Level {target_upgrade['level'] + 1} for {target_upgrade['cost']}$? (Y/N) ").lower()
        if confirmation not in ['y', 'yes']:
            print("Ok...")
            return False
        
        self.player.balance -= target_upgrade['cost']
        self.player.upgrades[target_upgrade_index]['level'] += 1
        print("Thank you for your purchase :)")

class Board:
    def __init__(self, height, width, players, pieces = []):
        self.height = height
        self.width = width
        self.players = players
        self.pieces = pieces
        self.bitboards = {}
        self.is_game_ended = False

    
    
    def get_is_game_ended(self):
        return self.is_game_ended

    
    def setup_bitboards(self, pieces):
        for player in self.players:
            for piece in pieces:
                if piece not in self.pieces:
                    self.pieces.append(piece)
                self.bitboards[f'{player.color}_{piece.name}'] = 0
        return True

    
    def set_piece(self, player, piece, coords):
        
        if not type(coords) == int:
            coords = coords[0] + (coords[1] - 1) * self.width
        self.bitboards[f'{player.color}_{piece.name}'] |= (1 << (self.height * self.width) - coords)
        return True

    
    def print_bitboards(self):
        for name, bitboard in self.bitboards.items():
            print(name, bitboard)
    
    def clear_square(self, coords):
        if not type(coords) == int:
            coords = coords[0] + (coords[1] - 1) * self.width
        for piece, bitboard in self.bitboards.items():
            
            if bitboard & (1 << (self.height * self.width) - coords) != 0:
                self.bitboards[piece] &= ~(1 << (self.height * self.width - coords))
        return


    def get_objects_from_bitboard_name(self, bitboard_name):
        
        color = bitboard_name[0]
        piece_name = bitboard_name[2:]
        resulting_player = self.players[list(map(lambda x: x.color, self.players)).index(color)]
        resulting_piece = self.pieces[list(map(lambda x: x.name, self.pieces)).index(piece_name)]
        return resulting_player, resulting_piece

    def get_bitboard(self, player, piece):
        return self.bitboards[f'{player.color}_{piece.name}']
    
    def get_piece_at_square(self, coords):
        
        if not type(coords) == int:
            coords = coords[0] + (coords[1] - 1) * self.width
        for piece, bitboard in self.bitboards.items():
            if bitboard & (1 << (self.height * self.width) - coords) != 0:
                return self.get_objects_from_bitboard_name(piece)
        return None, None
    
    
    
    
    def convert_letter_coord_to_number_coord(self, coord):
        expected_letters = [1]
        expected_numbers = [1,2]
        
        coord = coord.lower()
        letter_indexes = []
        for i in range(len(coord)):
            if 'a' <= coord[i] <= 'z':
                letter_indexes.append(i)
        number_indexes = []
        for i in range(len(coord)):
            if '0' <= coord[i] <= '9':
                number_indexes.append(i)

        
        if len(letter_indexes) not in expected_letters:
            return False
            
        if len(number_indexes) not in expected_numbers:
            return False
            
        
        if sorted(number_indexes) != list(range(min(number_indexes), max(number_indexes)+1)):
            return False
            
        resulting_number = ''
        for index in number_indexes:
            resulting_number += coord[index]
        resulting_number = int(resulting_number)

        resulting_letter = ''
        for index in letter_indexes:
            resulting_letter += coord[index]
        resulting_letter = resulting_letter

        
        if not (1 <= resulting_number <= self.height):
            return False
        if not ('a' <= resulting_letter <= chr(self.width + ord('a') - 1)):
            return False

        x = 'abcdefghijklmnopqrstuvwyxz'.index(resulting_letter) + 1
        y = resulting_number

        return [x,y]

    
    
    
    
    
    
    
    
    
    def print_board(self, flipped = False, buffer = 0, highlighted_squares = []):
        number_of_rows = self.height
        number_of_columns = self.width
        grid_array = []
        
        coords_line = [' ']
        for i in range (number_of_columns):
            coords = f'  {chr(65 + i)}  '
            coords_line.append(coords)
            coords_line.append(' ')
        coords_line = ''.join(coords_line)
        if flipped:
            coords_line = coords_line[::-1]
        grid_array.append(coords_line)
        
        
        first_line = ['╔']
        for i in range(number_of_columns-1):
            first_line.append('╦')
        first_line.append('╗')
        grid_array.append('═════'.join(first_line))

        for row in range(number_of_rows):
            
            row_array = ['║']
            for column in range(number_of_columns):
                row_array.append(' ')
                square_player, square_piece = self.get_piece_at_square([column+1, row+1])
                if flipped:
                    square_player, square_piece = self.get_piece_at_square([self.width-column, self.height - row])
                
                if not (square_player is None and square_piece is None):
                    
                    color_symbol = ' '
                    for color, symbol in color_symbols.items():
                        if square_player.color == color:
                            color_symbol = symbol
                    
                    row_array.append(f'/{color_symbol}\\')
                else:
                    row_array.append('   ')
                row_array.append(f' ║')
            if not flipped:
                row_array.append(' ' + str(row+1))
            grid_array.append(''.join(row_array))
            row_array = ['║']
            for column in range(number_of_columns):
                square_player, square_piece = self.get_piece_at_square([column+1, row+1])
                if flipped:
                    square_player, square_piece = self.get_piece_at_square([self.width-column, self.height - row])
                row_array.append(' ')
                if not (square_player is None and square_piece is None):
                    row_array.append(f'\\{square_piece.symbol}/')
                else:
                    row_array.append('   ')
                row_array.append(' ║')
            if flipped:
                row_array.append(' ' + str(self.height-row))
            grid_array.append(''.join(row_array))
            
            row_array = ['╠']
            for i in range(number_of_columns-1):
                row_array.append('╬')
            row_array.append('╣')
            grid_array.append('═════'.join(row_array))

        
        grid_array.pop()
        
        last_line = ['╚']
        for i in range(number_of_columns-1):
            last_line.append('╩')
        last_line.append('╝')
        grid_array.append('═════'.join(last_line))

        
        for square in highlighted_squares:
            symbol = '/'
            x = square[0]
            y = square[1]

            if flipped:
                x = self.width - x + 1
                y = self.height - y + 1

            new_line = ''
            for i in range(len(grid_array[3 * (y-1) + 1])):
                if 6 * x - 5 <= i < 6 * x:
                    new_line += symbol
                else:
                    new_line += grid_array[3 * (y-1) + 1][i]
            grid_array[3 * (y-1) + 1] = new_line
            
            new_line = ''
            for i in range(len(grid_array[3 * y + 1])):
                if 6 * x - 5 <= i < 6 * x:
                    new_line += symbol
                else:
                    new_line += grid_array[3 * y + 1][i]
            grid_array[3 * y + 1] = new_line
            
            new_line = ''
            for i in range(len(grid_array[3 * y - 2 + 1])):
                if i == 6 * (x-1) or i == 6 * x:
                    new_line += symbol
                else:
                    new_line += grid_array[3 * y - 2 + 1][i]
            grid_array[3 * y - 2 + 1] = new_line

            new_line = ''
            for i in range(len(grid_array[3 * y - 1 + 1])):
                if i == 6 * (x-1) or i == 6 * x:
                    new_line += symbol
                else:
                    new_line += grid_array[3 * y - 1 + 1][i]
            grid_array[3 * y - 1 + 1] = new_line


        
        for i in range(len(grid_array)):
            grid_array[i] = buffer * ' ' + grid_array[i]
        print('\n'.join(grid_array))
        return
    
    def account_for_blocking(self,target_square, possible_squares, active_player):
        
        for square in possible_squares:
            
            is_blocked = False
            if square[0] == target_square[0]:
                if square[1] > target_square[1]:
                    for i in range(1, square[1] - target_square[1] + 1):
                        if is_blocked:
                            if possible_squares.count(square) > 0:
                                possible_squares.remove(square)
                        if self.get_piece_at_square([square[0], target_square[1] + i]) != (None, None):
                            is_blocked = True
                else:
                    for i in range(1, target_square[1] - square[1] + 1):
                        if is_blocked:
                            if possible_squares.count(square) > 0:
                                possible_squares.remove(square)
                        if self.get_piece_at_square([square[0], square[1] + (target_square[1] - square[1] - i)]) != (None, None):
                            is_blocked = True
            
            is_blocked = False
            if square[1] == target_square[1]:
                if square[0] > target_square[0]:
                    for i in range(1, square[0] - target_square[0] + 1):
                        if is_blocked:
                            if possible_squares.count(square) > 0:
                                possible_squares.remove(square)
                        if self.get_piece_at_square([square[1], target_square[0] + i]) != (None, None):
                            is_blocked = True
                else:
                    for i in range(1, target_square[0] - square[0] + 1):
                        if is_blocked:
                            if possible_squares.count(square) > 0:
                                possible_squares.remove(square)
                        if self.get_piece_at_square([square[1], square[0] + (target_square[0] - square[0] - i)]) != (None, None):
                            is_blocked = True

            
            is_blocked = False
            if abs(target_square[0] - square[0]) == abs(target_square[1] - square[1]):
                if square[0] > target_square[0]: 
                    if square[1] > target_square[1]: 
                        for i in range(1,square[0] - target_square[0] + 1):
                            if is_blocked:
                                if possible_squares.count(square) > 0:
                                    possible_squares.remove(square)
                            if self.get_piece_at_square([target_square[0] + i, target_square[1] + i]) != (None, None):
                                is_blocked = True
                    else: 
                        for i in range(1,square[0] - target_square[0] + 1):
                            if is_blocked:
                                if possible_squares.count(square) > 0:
                                    possible_squares.remove(square)
                            if self.get_piece_at_square([target_square[0] + i, target_square[1] - i]) != (None, None):
                                is_blocked = True
                else: 
                    if square[1] > target_square[1]: 
                        for i in range(1,target_square[0] - square[0]+1):
                            if is_blocked:
                                if possible_squares.count(square) > 0:
                                    possible_squares.remove(square)
                            if self.get_piece_at_square([target_square[0] - i, target_square[1] + i]) != (None, None):
                                is_blocked = True
                    else: 
                        for i in range(1,target_square[0] - square[0]+1):
                            if is_blocked:
                                if possible_squares.count(square) > 0:
                                    possible_squares.remove(square)
                            if self.get_piece_at_square([target_square[0] - i, target_square[1] - i]) != (None, None):
                                is_blocked = True
            
            if self.get_piece_at_square(square)[0] is active_player:
                if possible_squares.count(square) > 0:
                    possible_squares.remove(square)
        return True

    





def end_game(player, piece, start_coords, end_coords, board):
    game_print(f'{board.players.index(player) + 1} ({board.players[(board.players.index(player)) % len(board.players)].color}) wins!')
    board.is_game_ended = True

def nexus_guard_destroyed(player, piece, start_coords, end_coords, board):
    board.players[(board.players.index(player)) % len(board.players)].balance += 7


nexus_capture = Gimmick('Nexus', 'Ends the game.', 'on_capture', end_game)
nexus_guard_capture = Gimmick('High Valued', 'When captured, the opposing player earns 10$.', 'on_capture', nexus_guard_destroyed)


pieces = [
    {'name': 'Nexus', 'symbol': '⛋',
        'description': 'The MOST important piece. Keep alive at all costs, or else you lose.',
        'movement_pattern': {'pattern': [0b00000,0b00100,0b01010,0b00100,0b00000],
                            'piece_position': [2,2]},
        'attack_pattern': {'pattern': [0b00000,0b00000,0b00000,0b00000,0b00000],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': False, 'cost': 999, 'unbuyable': True},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': [nexus_capture]},
        'rarity': None
        },
    {'name': 'Nexus Guard', 'symbol': '⛨',
        'description': 'Protects the Nexus. Takes 3 hits before death.',
        'movement_pattern': {'pattern': [0b00000,0b00000,0b01010,0b00100,0b00000],
                            'piece_position': [2,2]},
        'attack_pattern': {'pattern': [0b00000,0b00000,0b00000,0b00000,0b00000],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': False, 'cost': 999, 'unbuyable': True},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': None
        },
    {'name': 'Pawn', 'symbol': '♙',
        'description': 'just a pawn.',
        'movement_pattern': {'pattern': [0b00000,0b00100,0b00000,0b00000,0b00000],
                            'piece_position': [2,2]},
        'attack_pattern': {'pattern': [0b00000,0b01010,0b00000,0b00000,0b00000],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': True, 'cost': 1, 'unbuyable': False},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': COMMON
        },
    {'name': 'Scuffed Bishop', 'symbol': '♗',
        'description': 'A worse bishop...',
        'movement_pattern': {'pattern': [0b1000001,0b0100010,0b0010100,0b0000000,0b0010100,0b0100010,0b1000001],
                            'piece_position': [3,3]},
        'attack_pattern': {'pattern': [0b10001,0b01010,0b00000,0b01010,0b10001],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': True, 'cost': 3, 'unbuyable': False},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': RARE
        },
    {'name': 'Rookie', 'symbol': '♖',
        'description': 'An aspriring rook.',
        'movement_pattern': {'pattern': [0b0001000,0b0001000,0b0001000,0b1110111,0b0001000,0b0001000,0b0001000],
                            'piece_position': [3,3]},
        'attack_pattern': {'pattern': [0b00100,0b00100,0b11011,0b00100,0b00100],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': True, 'cost': 5, 'unbuyable': False},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': RARE
        },
    {'name': 'Long-reigning Queen', 'symbol': '♕',
        'description': 'A queen that\'s lost some of her edge over the years.',
        'movement_pattern': {'pattern': [0b1001001,0b0101010,0b0011100,0b1110111,0b0011100,0b0101010,0b1001001],
                            'piece_position': [3,3]},
        'attack_pattern': {'pattern': [0b10101,0b01110,0b11011,0b01110,0b10101],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': False, 'cost': 10, 'unbuyable': False},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': LEGENDARY
        },
    {'name': 'Buckshot', 'symbol': '⦾',
        'description': 'A shotgun. It\' literally a shotgun.',
        'movement_pattern': {'pattern': [0b1100011,0b0110110,0b0011100,0b0000000,0b0000000,0b0000000,0b0000000],
                            'piece_position': [3,3]},
        'attack_pattern': {'pattern': [0b01010,0b00100,0b00000,0b00100,0b01010],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': False, 'cost': 7, 'unbuyable': False},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': RARE
        },
    ]


new_pieces = []
for piece in pieces:
    new_pieces.append(Piece(**piece))
pieces = new_pieces





text_logs = []
def game_print(*args):
    text = ' '.join(args)
    print(text)
    text_logs.append(text)

def wash_screen():
    print('\n' * 100)


def game_input(*args):
    player_input = input(' '.join(args))
    if len(player_input) == 0:
        return ''
    
    print()
    if player_input.lower()[0] == '/':
        command = player_input.lower()[1::].split(' ')
        action = command[0]
        args = command[1::]

        
        if action == 'lookup': 
            underscore_piece_names = list(map(lambda x: '_'.join(x.name.split(' ')).lower(), pieces))
            for arg in args:
                if arg in underscore_piece_names:
                    pieces[underscore_piece_names.index(arg)].print_business_card()
                else:
                    print(f"'{arg}' is not a piece name. Make sure you replace spaces with underscores (_)")

        elif action == 'index':
            for piece in pieces:
                print('_'.join(piece.name.split(' ')), piece.symbol)

        elif action == 'logs':
            is_integer = True
            if not len(args) == 0:
                for character in args[0]:
                    if not '0' <= character <= '9':
                       is_integer = False
                if is_integer:
                    target_length = int(args[0])
                    logs_to_be_printed = []
                    index = -1
                    while len(logs_to_be_printed) < target_length:
                        if index <= -1 - len(text_logs):
                            logs_to_be_printed.append("There's nothing here... :(")
                        else:
                            if not text_logs[index] == '':
                                logs_to_be_printed.append(text_logs[index])
                        index -= 1
                    for i, log in enumerate(logs_to_be_printed):
                        print(f'[{i+1}] - {log}')
                else:
                    print("Invalid Integer")
            else:
                print("Please put a max_length")
        
        elif action == 'emoji':
            print(chr(128512 + random.randint(0,1000)))

        else:
            print(f"Invalid command: '{action}'")
        
        print()
        
        return game_input(*args)
    else:
        return player_input









def get_coordinate_from_player(board, text, required_list, unavaliable_message, exception = None):   
    if required_list == []:
        print("That piece is unavaliable!")
        return False
    print(text)
    player_input = game_input("")
    if player_input == exception:
        print("!!!")
        return True
    target_square = board.convert_letter_coord_to_number_coord(player_input)
    while (target_square is False) or (target_square not in required_list):
        if target_square is False: 
            print("That's not a valid coordinate!")
        else: 
            print(unavaliable_message)
        print(text)
        player_input = game_input("")
        target_square = board.convert_letter_coord_to_number_coord(player_input)
        if player_input == exception:
            return True
    return target_square

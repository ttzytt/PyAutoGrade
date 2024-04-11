from lolchess_class import *

board = Board(13, 7, [], [])

def convert_letter_coord_to_number_coord(coord, board):
    
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

    
    if not (1 <= resulting_number <= board.height):
        return False
    if not ('a' <= resulting_letter <= chr(board.width + ord('a') - 1)):
        return False

    x = 'abcdefghijklmnopqrstuvwyxz'.index(resulting_letter) + 1
    y = resulting_number

    return [x,y]




pieces = [
    {'name': 'Nexus', 'symbol': '⛋',
        'description': 'The MOST important piece. Keep alive at all costs, or else you lose.',
        'movement_pattern': {'pattern': [0b00000,0b00100,0b01010,0b00100,0b00000],
                            'piece_position': [2,2]},
        'attack_pattern': {'pattern': [0b00000,0b00000,0b00000,0b00000,0b00000],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': False, 'cost': 999, 'unbuyable': True},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': None
        },
    {'name': 'Nexus Guard', 'symbol': '⭑',
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
        'rarity': UNCOMMON
        },
    {'name': 'Rookie', 'symbol': '♖',
        'description': 'An aspriring rook.',
        'movement_pattern': {'pattern': [0b0001000,0b0001000,0b0001000,0b1110111,0b0001000,0b0001000,0b0001000],
                            'piece_position': [3,3]},
        'attack_pattern': {'pattern': [0b00100,0b00100,0b11011,0b00100,0b00100],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': True, 'cost': 5, 'unbuyable': False},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': UNCOMMON
        },
    {'name': 'Long-reigning Queen', 'symbol': '♕',
        'description': 'A queen that\'s lost some of her edge over the years.',
        'movement_pattern': {'pattern': [0b1001001,0b0101010,0b0011100,0b1110111,0b0011100,0b0101010,0b1001001],
                            'piece_position': [3,3]},
        'attack_pattern': {'pattern': [0b10101,0b01110,0b11011,0b01110,0b10101],
                            'piece_position': [2,2]},
        'mounting_details': {'starting': False, 'cost': 8, 'unbuyable': False},
        'gimmick_functions': {'movement': [], 'attack': [], 'mounting': [], 'on_capture': []},
        'rarity': RARE
        }
    ]

new_pieces = []
for piece in pieces:
    new_pieces.append(Piece(**piece))
pieces = new_pieces

# Custom Input Function
def game_input(text):
    player_input = input(text)
    if len(player_input) == 0:
        return ''
    if player_input.lower()[0] == '/':
        command = player_input.lower()[1::].split(' ')
        action = command[0]
        args = command[1::]

        if action == 'lookup':
            underscore_piece_names = list(map(lambda x: '_'.join(x.name.split(' ')).lower(), pieces))
            for arg in args:
                if arg in underscore_piece_names:
                    pieces[underscore_piece_names.index(arg)].print_business_card()
            return None
    else:
        return player_input

while True:
    print(game_input("text "))
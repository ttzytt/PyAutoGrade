



pieces = ['nexus', 'guard']

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        white_piece_bitboards = {}
        black_piece_bitboards = {}

    
    def setup_bitboards(self, pieces):
        for piece in pieces:
            self.white_piece_bitboards[f'W_{piece}'] = 0
        for piece in pieces:
            self.black_piece_bitboards[f'B_{piece}'] = 0

    def set_piece(self, color, piece, coords):
        
        if not type(coords) == int:
            coords = coords[0] + (coords[1] - 1) * self.width
        if color == 'W':
            self.white_piece_bitboards[f'W_{piece}'] |= 1 << (self.height * self.width) - coords
        else:
            self.black_piece_bitboards[f'B_{piece}'] |= 1 << (self.height * self.width) - coords

    def get_board_string(self, coordinates = False):
        
        if coordinates:
            
            
            alphabet = "abcdefghjilkmnopqrstuvwxyz"
            row_arr = ["   "]
            for i in range(self.length):
                
                row_arr.append(f" {alphabet[i].upper()}{alphabet[i].lower()}  ")
            board_string_arr = ["".join(row_arr)]
        else:
            board_string_arr = []
        board_string_arr.append("".join(['  ╔', '════╦' * (self.length - 1), '════╗']))

        for row in range(self.height):
            if coordinates:
                
                
                
                numbers = "123456789!@#$%^&*()"
                row_arr = [f"{numbers[row]}", " ║ "] 
            else:    
                row_arr = ["  ║ "]
            for column in range(self.width):
                if self.state[row][column] == "1":
                    row_arr.append('◯ ')
                elif self.state[row][column] == "-1":
                    row_arr.append('><')
                else:
                    row_arr.append('  ')
                row_arr.append( " ║ ")
            row_arr[-1] = " ║"
            board_string_arr.append("".join(row_arr))
            board_string_arr.append("".join(['  ╠', '════╬' * (self.length - 1), '════╣']))
            
        board_string_arr[-1] = ("".join(['  ╚', '════╩' * (self.length - 1), '════╝']))

        return "\n".join(board_string_arr)
    
def setup(pieces):
    pieces
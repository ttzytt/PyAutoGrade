


class Board:
    def __init__(self, height, length, win_amount):
        self.height = height
        self.length = length
        self.values = []
        self.win_amount = win_amount
        
        
        
        self.state = [[0 for x in range(length)] for x in range(height)]

    def check_win_space(self, height, length, win_amount, direction = None):
        if win_amount == 1:
            return self.state[height][length]
        else:
            is_valid_length = length < self.length - win_amount + 1
            is_valid_height = height < self.height - win_amount + 1
            
            if is_valid_length and direction in ["right",None]:
                if self.state[height][length] == self.state[height][length + 1]:
                    return self.check_win_space(height,length + 1, win_amount - 1, "right")
            
            if is_valid_height and direction in ["down",None]:
                if self.state[height][length] == self.state[height + 1][length]:
                    return self.check_win_space(height + 1,length , win_amount - 1, "down")
            
            if direction in ["diagonal",None]:
                if is_valid_length and is_valid_height and self.state[height][length] == self.state[height + 1][length + 1]:
                    return self.check_win_space(height + 1,length + 1, win_amount - 1, "diagonal")
                
            return 0

    def check_win(self):
        
        for i in range(self.height):
            for j in range(self.length):
                if not self.check_win_space(i,j, self.win_amount) == 0:
                    return self.check_win_space(i,j, self.win_amount)
        return 0
                
    def check_tie(self):
        for x in self.state:
            if 0 in x:
                return False
        return True
                
    def make_move(self, row, column, value):
        if value == 0:
            
            
            return False

        
        if self.state[row][column] == 0:
            self.state[row][column] = value
            if value not in self.values:
                self.values.append(value)
            return True
        else:
            
            return False
        
    def make_move_coords(self, number, letter, value):
        
        if number not in "123456789!@#$%^&*()" or letter.lower() not in "abcdefghjilkmnopqrstuvwxyz":
            return False
        if number == '' or letter == '':
            return False
        row_index = "123456789!@#$%^&*()".index(number)
        column_index = "abcdefghjilkmnopqrstuvwxyz".index(letter.lower())
        
        if row_index >= self.height or column_index >= self.length:
            return False
        return self.make_move(row_index, column_index, value)
        
    def get_board_string(self, coordinates = False):
        '''
        Example Board:
           Aa   Bb
         ╔════╦════╦════╗
         ║ ◯ ║    ║    ║
         ╠════╬════╬════╣
         ║ <> ║    ║    ║
         ╠════╬════╬════╣
         ║    ║    ║    ║
         ╚════╩════╩════╝
        '''
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
            for column in range(self.length):
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

def game_loop():
    print(game.get_board_string(True))
    move = input("Player 1 : ")
    while not game.make_move_coords(move[1], move[0], '1'):
        print("That's not a valid move.")
        move = input("Player 1 : ")
    if game.check_win():
        print("Player 1 Wins!!!")
        return False
    elif game.check_tie():
        print("Tied!")
        return False
    else:
        print(game.get_board_string(True))
        move = input("Player 2 : ")
        while not game.make_move_coords(move[1], move[0], '-1'):
            print("That's not a valid move.")
            move = input("Player 2 : ")
        if game.check_win():
            print("Player 2 Wins!!!")
            return False
        elif game.check_tie():
            print("Tied!")
            return False
    return True


print("Welcome to Better Tic-Tac-Toe!")
game = Board(int(input("# of columns: ")),
             int(input("# of rows: ")),
             int(input("# in a row to win: ")))
print("Enter moves with the notation Letter Number (for example: b3, a6, c9)")

playing = True

while playing:
    playing = game_loop()
print(game.get_board_string(True))


    

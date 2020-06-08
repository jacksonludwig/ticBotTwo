class Board:
    MAGIC_SQUARE = [4, 9, 2, 3, 5, 7, 8, 1, 6]
    SYM_X = "X"
    SYM_O = "O"

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def format_board(self):
        row1 = f"{self.board[0]} | {self.board[1]} | {self.board[2]}"
        row2 = f"{self.board[3]} | {self.board[4]} | {self.board[5]}"
        row3 = f"{self.board[6]} | {self.board[7]} | {self.board[8]}"
        return f"{row1}\n{row2}\n{row3}"

    def is_spot_taken(self, position):
        return isinstance(self.board[position], int)

    def is_position_okay(self, position):
        return position > 0 and position < 10

    def is_symbol_okay(self, symbol):
        return symbol == SYM_X or symbol == SYM_O

    def take_move(self, symbol, position):
        symbol = symbol.upper()
        position = position - 1
        self.board[position] = symbol

    def check_tie(self):
        for i in range(len(self.board)):
            if not is_spot_taken(i):
                return False
        return True

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
        return f"```{row1}\n{row2}\n{row3}```"

    def normalize_inputs(self, symbol, position):
        return (symbol.upper(), int(position))

    def is_spot_taken(self, position):
        return isinstance(self.board[position], int)

    def is_position_okay(self, position):
        return position > 0 and position < 10

    def is_symbol_okay(self, symbol):
        return symbol == SYM_X or symbol == SYM_O

    def take_move(self, symbol, position):
        position = position - 1
        self.board[position] = symbol

    def is_tie(self):
        for i in range(len(self.board)):
            if not is_spot_taken(i):
                return False
        return True

    def __magic_square_check(self, symbol, i, j, k):
        if i != j and i != k and j != k:
            if (board[i], board[j], board[k]) == (symbol, symbol, symbol):
                if MAGIC_SQUARE[i] + MAGIC_SQUARE[j] + MAGIC_SQUARE[k] == 15:
                    return True

    def is_win(self, symbol):
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    self.__magic_square_check(symbol, i, j, k)

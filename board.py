class Board:
    MAGIC_SQUARE = [4, 9, 2, 3, 5, 7, 8, 1, 6]

    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def format_board(self):
        row1 = f"{self.board[0]} | {self.board[1]} | {self.board[2]}"
        row2 = f"{self.board[3]} | {self.board[4]} | {self.board[5]}"
        row3 = f"{self.board[6]} | {self.board[7]} | {self.board[8]}"
        return f"```{row1}\n{row2}\n{row3}```"

    def is_spot_open(self, position):
        return isinstance(self.board[position], int)

    def take_move(self, symbol, position):
        position = int(position) - 1
        self.board[position] = symbol

    def is_tie(self):
        for i in range(len(self.board)):
            if self.is_spot_open(i):
                return False
        return True

    def __magic_square_check(self, board, symbol, i, j, k):
        MAGIC_SQUARE = self.MAGIC_SQUARE
        if i != j and i != k and j != k:
            if (board[i], board[j], board[k]) == (symbol, symbol, symbol):
                if MAGIC_SQUARE[i] + MAGIC_SQUARE[j] + MAGIC_SQUARE[k] == 15:
                    return True
        return False

    def is_win(self, symbol):
        for i in range(0, 9):
            for j in range(0, 9):
                for k in range(0, 9):
                    if self.__magic_square_check(self.board, symbol, i, j, k):
                        return True
        return False

from const import *
from square import Square


class board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(Cols)] # создали для каждого солбца базовое значение, с которым мы будем работать.
        self._crate()

    def _crate(self):
        for row in range(Rows):
            for col in range(Cols):
                self.squares[row][col] = Square(row, col)

    def _add_piece(self, color):
        pass

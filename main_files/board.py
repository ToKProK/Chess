from const import *
from square import Square
from piece import *


class board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(Cols)] # создали для каждого солбца базовое значение, с которым мы будем работать.
        self._crate()
        self._add_piece('white')
        self._add_piece('black')

    def _crate(self):
        for row in range(Rows):
            for col in range(Cols):
                self.squares[row][col] = Square(row, col)
                

    def _add_piece(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        #метод для пешки

        for col in range(Cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        
        #метод для конь
        self.squares[row_other][1] = Square(row_other, 1, knight(color))
        self.squares[row_other][6] = Square(row_other, 6, knight(color))
        
        #метод для слонов
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        #метод для ладьи
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        #метод для королевы
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))


        #метод для короля
        self.squares[row_other][4] = Square(row_other, 4, king(color))


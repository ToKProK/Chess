from const import *
from square import Square
from piece import *

# Данный класс представляет доску, которя является массивом "squares"
class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(Cols)] # создали для каждого солбца базовое значение, с которым мы будем работать.
        self._create()
        self._add_piece('white')
        self._add_piece('black')

    def _create(self):
        for row in range(Rows):
            for col in range(Cols):
                self.squares[row][col] = Square(row, col)
                

    def _add_piece(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0) 

        #метод для пешки
        for col in range(Cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        
        #метод для конь
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        
        #метод для слонов
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        #метод для ладьи
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        #метод для королевы
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))


        #метод для короля
        self.squares[row_other][4] = Square(row_other, 4, King(color))


    def cal_moves(self, piece, row, col):
        if isinstance(piece, Pawn):  # piece.nam
            pass
        elif isinstance(piece, Knight):
            pass
        elif isinstance(piece, Bishop):
            pass
        elif isinstance(piece, Rook):
            pass
        elif isinstance(piece, Queen):
            pass
        elif isinstance(piece, King):
            pass
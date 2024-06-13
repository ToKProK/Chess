from const import *
from square import Square
from piece import *
from move import Move

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

        def pawn_moves():
            step = 1 if piece.moved else 2
            # Вертикальное движение
            start = row + piece.dir
            end = row + (piece.dir * (step + 1)) # + 1, поскольку в цикле for на 1 меньше
            for move_row in range(start, end, piece.dir):
                if Square.in_range(move_row): # Проверка каждого хода на выход фигуры за игровую доску
                    if self.squares[move_row][col].isempty(): # Проверям, что клетка пустая
                        initial = Square(row, col)

                        final = Square(move_row, col)

                        move = Move(initial, final)

                        piece.add_move(move)
                    else:
                        break
            # Диогональное движение
            move_row = 
            
        def knight_moves():
            # В идеале у коня 8 возможных ходов
            possible_moves = [
                (row - 2, col + 1),
                (row - 1, col + 2),
                (row + 1, col + 2),
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row + 1, col - 2),
                (row - 1, col - 2),
                (row - 2, col - 1),
            ]
            for pos_move in possible_moves:
                pos_move_row, pos_move_col = pos_move

                if Square.in_range(pos_move_row, pos_move_col): # Проверка каждого хода на выход фигуры за игровую доску
                    if self.squares[pos_move_row][pos_move_col].empty_or_enemy(piece.color):# Проверка каждого хода на наличие противника или пустой клетки
                        # Фиксирую позицию выбранной фигуры
                        initial = Square(row, col)
                        # Фикирую все возможный ходы фигуры
                        final = Square(pos_move_row, pos_move_col) # Недоделал фигуры(piece)

                        move = Move(initial, final)

                        piece.add_move(move)
                        

        if isinstance(piece, Pawn):  # piece.name == 'pawn' (одно и тоже)
            pawn_moves()
        elif isinstance(piece, Knight): # Конь
            knight_moves()
        elif isinstance(piece, Bishop):
            pass
        elif isinstance(piece, Rook):
            pass
        elif isinstance(piece, Queen):
            pass
        elif isinstance(piece, King):
            pass
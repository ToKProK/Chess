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

        def pawn_moves(): # Движения пешки
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
                else:
                    break
            # Диогональное движение
            move_row = row + piece.dir
            move_cols = [col-1,col+1]
            for move_col in move_cols:
                if Square.in_range(move_row, move_col):  # Проверка на выход за карту
                    if self.squares[move_row][move_col].has_enemy_piece(piece.color): # Проверка на нахождение врага на клетке
                        initial = Square(row, col)
                        final = Square(move_row, move_col)

                        move = Move(initial, final)

                        piece.add_move(move)
        
        def king_moves():
            possible_moves = [ 
                (row - 1, col + 0),
                (row - 1, col + 1),
                (row + 0, col + 1),
                (row + 1, col + 1),
                (row + 1, col + 0),
                (row + 1, col - 1),
                (row + 0, col - 1),
                (row - 1, col - 1),
            ]
            for pos_move in possible_moves:
                move_row, move_col = pos_move

                if Square.in_range(move_row, move_col):
                    if self.squares[move_row][move_col].empty_or_enemy(piece.color):
                        initial = Square(row, col)
                        # Фикирую все возможный ходы фигуры
                        final = Square(move_row, move_col) # Недоделал фигуры(piece)

                        move = Move(initial, final)

                        piece.add_move(move)
            
        def knight_moves(): # Движения коня
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
                        
        def straightline_move(incs): # Передвижения по прямой линии (inc - направление прямой линии)
            for inc in incs:
                inc_row, inc_col = inc
                move_row = row + inc_row
                move_col = col + inc_col
                while True:
                    if Square.in_range(move_row, move_col): # Проверка на выход за карту
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        move = Move(initial, final) 
                        # Пустая клетка (add_move)
                        if self.squares[move_row][move_col].isempty(): # Проверка на пустую клетку
                            piece.add_move(move)
                        # Протиник (add_move + break)
                        if self.squares[move_row][move_col].has_enemy_piece(piece.color):
                            piece.add_move(move)
                            break # После встречи с противником линия должна остановиться
                        # Союзник (break)
                        if self.squares[move_row][move_col].has_team_piece(piece.color):
                            break # После встречи с противником линия должна остановиться
                    else: # Если ушел за пределы карту
                        break
                    move_row += inc_row
                    move_col += inc_col


                        
        if isinstance(piece, Pawn):  # piece.name == 'pawn' (одно и тоже)
            pawn_moves()
        elif isinstance(piece, Knight): # Конь
            knight_moves()
        elif isinstance(piece, Bishop):
            bishop_incs = [
                (-1, 1), # Вверх вправо
                (-1, -1), # Вверх влево
                (1, 1), # Вниз вправо
                (1, -1), # Вниз влево
            ]
            straightline_move(bishop_incs)
        elif isinstance(piece, Rook):
            rook_incs = [
                (-1, 0), # Вверх
                (0, 1), # Вправо
                (1, 0), # Вниз
                (0, -1) # Влево
            ]
            straightline_move(rook_incs)
        elif isinstance(piece, Queen):
            queen_incs = [
                (-1, 1), # Вверх вправо
                (-1, -1), # Вверх влево
                (1, 1), # Вниз вправо
                (1, -1), # Вниз влево
                (-1, 0), # Вверх
                (0, 1), # Вправо
                (1, 0), # Вниз
                (0, -1) # Влево
            ]
            straightline_move(queen_incs)
        elif isinstance(piece, King):
            king_moves()
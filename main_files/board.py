from const import *
from square import Square
from piece import *
from move import Move
import copy
# Данный класс представляет доску, которя является массивом "squares"
class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(Cols)] # создали для каждого солбца базовое значение, с которым мы будем работать.
        self._create()
        self._add_piece('white')
        self._add_piece('black')
        self.last_move = None

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


    def cal_moves(self, piece, row, col, bool=True):

        def pawn_moves(): # Движения пешки
            step = 1 if piece.moved else 2
            # Вертикальное движение
            start = row + piece.dir
            end = row + (piece.dir * (step + 1)) # + 1, поскольку в цикле for на 1 меньше
            for move_row in range(start, end, piece.dir):
                if Square.in_range(move_row): # Проверка каждого хода на выход фигуры за игровую доску
                    if self.squares[move_row][col].isempty(): # Проверям, что клетка пустая
                        # Фиксирум изначальную позицию и новую
                        initial = Square(row, col)
                        final = Square(move_row, col)
                        # Создаём новый доступный ход
                        move = Move(initial, final)

                        # Проверяем ход (ход может быть недоступен из-за моментального шаха и мата)
                        if bool: # Данное условие позволяет вызывать метод только через файл main
                            if not self.in_check(piece, move):
                                piece.add_move(move)
                            else:
                                break
                        else:
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
                        final_piece = self.squares[move_row][move_col].piece
                        final = Square(move_row, move_col, final_piece)

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

                        # Проверяем ход (ход может быть недоступен из-за моментального шаха и мата)
                        if bool: # Данное условие позволяет вызывать метод только через файл main
                            if not self.in_check(piece, move):
                                piece.add_move(move)
                            # else:
                            #     break
                        else:
                            piece.add_move(move) 
            # рокировка
            if not piece.moved:
                # Левая рокировка
                    left_rook = self.squares[row][0].piece
                    if isinstance(left_rook, Rook):
                        if not left_rook.moved:
                            for i in range(1, 4):
                                if self.squares[row][i].has_piece(): # Другие фигуры перекрывают рокировку
                                    break
                                if i == 3:
                                    piece.left_rook = left_rook

                                    # Передвижение ладьи
                                    initial = Square(row, 0)
                                    final = Square(row, 3)
                                    moveR = Move(initial, final)
                                     
                                    # Передвижение короля
                                    initial = Square(row, col)
                                    final = Square(row, 2)
                                    moveK = Move(initial, final)
                                    

                                    
                                    # Проверяем ход (ход может быть недоступен из-за моментального шаха и мата)
                                    if bool: # Данное условие позволяет вызывать метод только через файл main
                                        if not self.in_check(piece, moveR) and not self.in_check(left_rook, moveK):
                                            # Добавляем ход ладье
                                            left_rook.add_move(moveR) 
                                            # Добавляем ход Королю
                                            piece.add_move(moveK)
                                        else:
                                            break
                                    else:
                                            # Добавляем ход ладье
                                            left_rook.add_move(moveR) 
                                            # Добавляем ход Королю
                                            piece.add_move(moveK)
                # Правая рокировка
                    right_rook = self.squares[row][7].piece
                    if isinstance(right_rook, Rook):
                        if not right_rook.moved:
                            for i in range(5, 7):
                                if self.squares[row][i].has_piece(): # Другие фигуры перекрывают рокировку
                                    break
                                if i == 6:
                                    piece.right_rook = right_rook

                                    # Передвижение ладьи
                                    initial = Square(row, 7)
                                    final = Square(row, 5)
                                    moveR = Move(initial, final)
                                    
                                    # Передвижение короля
                                    initial = Square(row, col)
                                    final = Square(row, 6)
                                    moveK = Move(initial, final) 
                                    



                                    # Проверяем ход (ход может быть недоступен из-за моментального шаха и мата)
                                    if bool: # Данное условие позволяет вызывать метод только через файл main
                                        if not self.in_check(piece, moveR) and not self.in_check(right_rook, moveK):
                                            # Добавляем ход ладье
                                            right_rook.add_move  (moveR) 
                                            # Добавляем ход Королю
                                            piece.add_move(moveK)
                                        else:
                                            break
                                    else:
                                            # Добавляем ход ладье
                                            right_rook.add_move(moveR) 
                                            # Добавляем ход Королю
                                            piece.add_move(moveK)
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
                        final_piece = self.squares[pos_move_row][pos_move_col].piece
                        final = Square(pos_move_row, pos_move_col, final_piece) # Недоделал фигуры(piece)

                        move = Move(initial, final)

                        # Проверяем ход (ход может быть недоступен из-за моментального шаха и мата)
                        if bool: # Данное условие позволяет вызывать метод только через файл main
                            if not self.in_check(piece, move):
                                piece.add_move(move)

                        else:
                            piece.add_move(move)
                        
        def straightline_move(incs): # Передвижения по прямой линии (inc - направление прямой линии)
            for inc in incs:
                inc_row, inc_col = inc
                move_row = row + inc_row
                move_col = col + inc_col
                while True:
                    if Square.in_range(move_row, move_col): # Проверка на выход за карту
                        initial = Square(row, col)
                        final_piece = self.squares[move_row][move_col].piece
                        final = Square(move_row, move_col, final_piece)
                        move = Move(initial, final) 
                        # Пустая клетка (add_move)
                        if self.squares[move_row][move_col].isempty(): # Проверка на пустую клетку
                            # Проверяем ход (ход может быть недоступен из-за моментального шаха и мата)
                            if bool: # Данное условие позволяет вызывать метод только через файл main
                                if not self.in_check(piece, move):
                                    piece.add_move(move)
                            else:
                                piece.add_move(move)
                        # Протиник (add_move + break)
                        elif self.squares[move_row][move_col].has_enemy_piece(piece.color):
                                                        # Проверяем ход (ход может быть недоступен из-за моментального шаха и мата)
                            if bool: # Данное условие позволяет вызывать метод только через файл main
                                if not self.in_check(piece, move):
                                    piece.add_move(move)
                            else:
                                piece.add_move(move)
                            break # После встречи с противником линия должна остановиться
                        # Союзник (break)
                        elif self.squares[move_row][move_col].has_team_piece(piece.color):
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
    
    def valid_move(self, piece, move):
        return move in piece.moves

    def chek_promotion(self, piece, final):
        # Пешка в королеву
        if final.row == 0 or final.row == 7:
            self.squares[final.row][final.col].piece = Queen(piece.color)
    def castling(self, initial, final):
        return abs(initial.col - final.col) == 2
    # Данный метод вызывается в этом файле в методе cal_move
    def in_check(self, piece, move): # Данный метод позволит запрещать делать ходы, которые приведут к немедленному порожению
        temp_piece = copy.deepcopy(piece)# Копируем фигуру
        temp_board = copy.deepcopy(self)# Копируем доску
        temp_board.move(temp_piece, move) # Делаем ход, который попадает в функцию (через переменную 'move')

        for row in range(Rows):
            for col in range(Cols):
                if temp_board.squares[row][col].has_enemy_piece(piece.color): # Перебираем всю доску в поисках фигур противника
                    p = temp_board.squares[row][col].piece # Переменная с фигурой соперника
                    temp_board.cal_moves(p, row, col, bool=False) # Прощитываем все ходы доступные фигуре
                    for m in p.moves:
                        if isinstance(m.final.piece, King): # Если фигура может убить короля 
                            return True
        return False

    def check_finish(self, color):
        temp_board = copy.deepcopy(self)# Копируем доску
        for row in range(Rows):
            for col in range(Cols):
                if temp_board.squares[row][col].has_team_piece(color): # Перебираем всю доску в поисках союзных фигур
                    p = temp_board.squares[row][col].piece # Переменная с фигурой соперника
                    temp_board.cal_moves(p, row, col, bool=True)
                    if p.moves:
                        return False
        return True
                        
                        


    def move(self, piece, move):
        initial =  move.initial
        final = move.final 

        # Обнавляем доску массива squares
        self.squares[initial.row][initial.col].piece = None # Там где раньше находилась фигура теперь None
        self.squares[final.row][final.col].piece = piece # В новом положение появляется фигура
        
        if isinstance(piece, Pawn):
            self.chek_promotion(piece, final) 
        
        if isinstance(piece, King):
            if self.castling(initial, final):
                dif =  final.col - initial.col
                rook = piece.left_rook if (dif < 0) else piece.right_rook
                self.move(rook, rook.moves[-1]) 
        # move
        piece.moved = True

        # Очищаем возможные ходы (поменяли позицию -> другие возможные ходы)
        piece.clear_moves()

        self.last_move = move

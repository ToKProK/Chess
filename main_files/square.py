class Square: # Класс клетки, у которой есть свой ряд(row) и столбец(col)
              # Также ситуативно может быть фигура(piece), которя находится на клетке

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col 
        self.piece = piece 

    def __eq__(self, move):
        return self.row == move.row and self.col == move.col 

    def has_piece(self): # Получаем True если есть фигура
        return self.piece != None
    
    def isempty(self): # Получаем True если клетка пуста
        return not self.has_piece() 

    def has_enemy_piece(self, color):
        return self.has_piece() and self.piece.color != color # Получаем True если на клетке фигуру соперника
    
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color # Получаем True если на клетке фигуру союзника

    def empty_or_enemy(self, color): # Объеженил проерку двух методов выше
        return self.isempty() or self.has_enemy_piece(color)
    

    @staticmethod
    def in_range(*args): #*args метод принимает неогранниченное(условно) кол-во данных
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
    
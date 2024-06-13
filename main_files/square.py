class Square: # Класс клетки, у которой есть свой ряд(row) и столбец(col)
              # Также ситуативно может быть фигура(piece), которя находится на клетке

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col 
        self.piece = piece 

    def has_piece(self): # Получаем True если есть фигура
        return self.piece != None
    
    def isempty(self): # Получаем True если клетка пуста
        return not self.has_piece() 

    def has_riva_piece(self, color):
        return self.has_piece() and self.piece.color != color # Получаем True если выбрали фигуру соперника

    def empty_or_enemy(self, color): # Объеженил проерку двух методов выше
        return self.isempty() or self.has_riva_piece(color)
    

    @staticmethod
    def in_range(*args): #*args метод принимает неогранниченное(условно) кол-во данных
        for arg in args:
            if arg < 0 or arg > 7:
                return False
        return True
    
class Square: # Класс клетки, у которой есть свой ряд(row) и столбец(col)
              # Также ситуативно может быть фигура(piece), которя находится на клетке

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col 
        self.piece = piece 

    def has_piece(self):
        return self.piece != None
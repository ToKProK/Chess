import os

class Piese:
    def __init__(self, name, color, value, texture, texture_rect=None):
        self.name = name
        self.color = color
        if color == 'white':
            value_sing = 1
        else:
            value_sing = -1
        self.value = value * value_sing # Таким образом value у черных юут отрицательное, а у белых положительное
        self.moves = []
        self.moved = False
        self.set_texture()
        self.texture_rect = texture_rect

    def set_textur(self, size=80):
        self.texture = os.path.join(f"assets/images/imgs-{size}px/{self.color}_{self.name}.png")

    def add_move(self, move):
        self.moves.append(move)



class Pawn(Piese):
    def __init__(self, color):
        if color == "white":
            self.dir = -1
        else:
            self.dir = 1
        super.__init__('pawn', color, 1.0)

class Knight(Piese):
    def __init__(self, color):
        super().__init__("knight", color, 3.0)

class Bishop(Piese):
    def __init__(self, color):
        super().__init__("bishop", color, 3.001)

class Rook(Piese):
    def __init__(self, color):
        super().__init__("rook", color, 5.0)

class Queen(Piese):
    def __init__(self, color):
        super().__init__("queen", color, 9.0)

class King(Piese):
    def __init__(self, color):
        super().__init__("king", color, 10000.0)
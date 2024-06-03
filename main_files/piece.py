
class Piese:
    
    def __init__(self, name, color, value, texture, teture_rect=None):
        pass

class Pawn(Piese):

    def __init__(self, color):
        if color == "white":
            self.dir = -1
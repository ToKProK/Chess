class Move():
    def __init__(self, initial, moves):
        self.initial = initial # Расположение самой фигуры 
        self.final = moves # Возвожный ход

    def __eq__(self, moves):
        return self.initial == moves.initial and self.final == moves.final
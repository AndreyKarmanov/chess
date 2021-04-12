# This is chess
# Need for Andrey:
    # available moves for currently selected pieces
    # list of where all the pieces are 

class Spot:
    pass

class Pieces:
    def __init__(self, colour):
        self._colour = colour

class Rook(Pieces):
    pass

class Knight(Pieces):
    pass

class Bishop(Pieces):
    pass

class King(Pieces):
    pass

class Queen(Pieces):
    pass

class Pawn(Pieces):
    pass

class Board:
    def __init__(self):
        self._boxes = [[] for i in range(8)]

class Player:
    pass

class Move:
    pass

class Game:
    pass

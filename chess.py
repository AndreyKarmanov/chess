# This is chess
# Need for Andrey:
    # available moves for currently selected pieces
    # list of where all the pieces are 

class Spot:
    def __init__(self, piece, x, y):
        self._piece = piece
        self._x = x
        self._y = y

    def getPiece():
        return self._piece

    def setPiece(p):
        self._piece = p

    def getX():
        return self._x

    def setX():
        self._x = x

    def getY():
        return self._y

    def setY():
        self._y = y



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
    pass

class Player:
    pass

class Move:
    pass

class Game:
    pass

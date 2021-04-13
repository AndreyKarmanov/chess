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
    def __init__(self):
        self._boxes = [['' for i in range(8)] for i in range(8)]

    def resetBoard(self): #! put this in init method?
        # Pieces
        colours = ((0, True), (7, False))
        pieces = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
        for info in colours:
            for i in range(8):
                self._boxes[info[0]][i] = Spot(pieces[i](info[1]), info[0], i)

        # Pawns
        for i in range(8):
            self._boxes[1][i] = Spot(Pawn(True), 1, i)
            self._boxes[6][i] = Spot(Pawn(False), 6, i)

        # Empty 
        for j in range(2, 6):
            for i in range(8):
                self._boxes[j][i] = Spot(None, j, i)

class Player:
    pass

class Move:
    pass

class Game:
    pass

board = Board()
board.resetBoard()
print(board._boxes)
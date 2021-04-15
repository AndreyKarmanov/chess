# This is chess
# Need for Andrey:
    # available moves for currently selected pieces
    # list of where all the pieces are 

class Spot:
    def __init__(self, piece, x, y):
        self._piece = piece
        self._x = x
        self._y = y

    def getPiece(self): #you have to pass in self if not a static method.
        return self._piece

    def setPiece(self, p):
        self._piece = p

    def getX(self):
        return self._x

    def setX(self):
        self._x = x

    def getY(self):
        return self._y

    def setY(self):
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
        # Pieces and Pawns
        colours = ((0, 1, True), (7, 6, False))
        pieces = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
        for info in colours:
            for i in range(8):
                self._boxes[info[0]][i] = Spot(pieces[i](info[2]), info[0], i)
                self._boxes[info[1]][i] = Spot(Pawn(info[2]), info[1], i)

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

for row in board._boxes:
    for peice in row:
        print(peice.getPiece())

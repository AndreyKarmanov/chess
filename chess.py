# This is chess
# Need for Andrey:
# available moves for currently selected pieces
# list of where all the pieces are > maybe we jsut don't bother and I make it simpler but less efficent.

"""

tl;dr 
got rid of spot class, moved the functionality to pieces class
class game is now class chess, and has board's resetboard() method
need to implement getMoves() for each piece (returning a list of x/y coords like I did in pawn class)

you can check out gameWindow, there is one bug that I didn't bother fixing as this redesign was coming up but it is kinda cool

What I changed:
1. I got rid of the "spot" class 
> it only provided a x/y coordinate
> I moved the x/y fields into the pieces class, so now every pawn, rook etc. has an x/y stored inside it.
> we need that x/y coordinate in the individual pieces in order to calculate possible moves (and put them in a list for me)

2. I renamed class Game to class Chess
> perhaps we could make a simple class called Game and extend that with chess
> but if we aren't then we need to be more specific with what exactly the class does 

3. I moved the resetboard() from class board to class chess
> board class is very broad and shouldn't have a chess-specific method in it 
> this is perfect because we just changed Game to Chess so the method has a nice home. 

What the plan is for now: (if something doesn't make sense just ask, or if you think something could be better/more intuitive also tell me)
1. have each piece have a getMoves() method that returns the possible moves for that piece in a list [(x,y), (x2,y2)... ]
> look at the method I made for pawn
> whenever a player picks up a piece I will call this method and highlight the squares that they can put the piece on 
> I will only allow them to move to these squares. (this simplifies the move method in the chess class)

2. create a way of actually running the game
> Normally in a game we have to wait for some sort of input ( in this case a chess move )
> and program would wait on input("what is your name")
> but since this is graphicsal we can't just wait on the name, as the window has to be updated/checked for clicks
> this is a tomorrow problem 

3. win checking?
"""


class Board:
    def __init__(self, rows, cols):
        self._boxes = [['' for i in range(cols)] for i in range(rows)]


class Pieces:
    def __init__(self, colour, x, y):
        self._colour = colour
        self.x = x
        self.y = y

    def withinBounds(self, x, y):
        return 0 <= x <= 7 and 0 <= y <= 7

class Discrete(Pieces):
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def discreteMovement(self, possible, boxes: list):
        moves = []
        for move in possible:
            x = self.x + move[0]
            y = self.y + move[1]
            if self.withinBounds(x, y) is True: # is there no other way of doing it? 'and' didn't work
                if boxes[y][x] is None or boxes[y][x]._colour != self._colour: 
                    moves.append((x, y))
        return moves
        

class Continuous(Pieces): 
    pass

class Knight(Discrete):
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def getMoves(self, boxes: list):
        possible = ((1, 2), (-1, -2), (1, -2), (-1, 2), (2, 1), (-2, -1), (-2, 1), (-1, 2))
        moves = self.discreteMovement(possible, boxes)
        return moves

class King(Discrete):
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)

    def getMoves(self, boxes: list):
        possible = ((0, 1), (1, 0), (0, -1), (-1, 0))
        moves = self.discreteMovement(possible, boxes)
        return moves

class Pawn(Discrete):
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.moved = False

    def getMoves(self, boxes: list):
        moves = []

        # pawn is unique, as it can only move towards the enemy.
        if self._colour: direction = -1
        else: direction = 1

        y = self.y + direction

        # checks if the square ahead of it is free
        if self.withinBounds(self.x, y) is True:
            if boxes[y][self.x] is None: moves.append((self.x, y))   

        # checks if there's an oposing piece to take
        for side in (1, -1):
            if self.withinBounds(self.x + side, y) is True:
                check = boxes[y][self.x + side]
                if check and check._colour != self._colour: moves.append((self.x + side, y)) 

        return moves

class Rook(Continuous):
    pass

class Bishop(Continuous):
    pass

class Queen(Continuous):
    pass

class Player:
    pass

class Chess:
    def __init__(self, white: Player, black: Player):
        self.board = Board(8, 8)
        self.resetBoard()

        # white player and black player placeholders (these guys can store their individual pieces maybe)
        self.white = white
        self.black = black

    def move(self, startX, startY, endX, endY):

        # foolproof method for testing
        if startX == endX and startY == endY:
            return

        # Moves and deletes the piece that was at the landing square (if any)
        self.board._boxes[endY][endX] = self.board._boxes[startY][startX]
        self.board._boxes[startY][startX] = None
        print(f'Moved ({startX}, {startY}) to ({endX}, {endY})')
        print(self.board._boxes[startY][startX],
              self.board._boxes[endY][endX], "swapped")
        self.board._boxes[endY][endX].x = endX
        self.board._boxes[endY][endX].y = endY

        # Since the pawn just moved, it isn't allowed to move 2 squares again.
        if isinstance(self.board._boxes[endY][endX], Pawn):
            self.board._boxes[endY][endX].moved = True

        # if king.castling(): > logic for moving other pieces is contained within king class? not sure the best way to do this part tbh.

    # test method please ignore
    def printBoard(self):
        for row in self.board._boxes:
            print([type(x) for x in row])

    # cool way of setting it up
    def resetBoard(self):  # ! put this in init method?
        # Pieces and Pawns
        colours = ((0, 1, False), (7, 6, True))
        pieces = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
        for info in colours:
            for i in range(8):
                self.board._boxes[info[0]][i] = pieces[i](info[2], i, info[0])
                self.board._boxes[info[1]][i] = Pawn(info[2],  i, info[1])

        # Empty
        for j in range(2, 6):
            for i in range(8):
                self.board._boxes[j][i] = None

    def getBoard(self):
        return self.board._boxes

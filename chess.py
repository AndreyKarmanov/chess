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
    def __init__(self, colour, x, y):
        super().__init__(colour, x, y)
        self.moved = False

    # takes a Board._boxes list and returns the possible moves that this piece can make.
    def getMoves(self, boxes: list):
        moves = []

        # pawn is unique, as it can only move towards the enemy.
        if self._colour:
            direction = 1
        else:
            direction = -1

        # checks if the square ahead of it is free or if ahead and diagonal have oposing pieces 
        if boxes[self.y + direction][self.x] is None:
            moves.append((self.y + direction, self.x))
        elif boxes[self.y + direction][self.x + 1]._colour != self._colour:
            moves.append((self.y + direction, self.x + 1))
        elif boxes[self.y + direction][self.x - 1]._colour != self._colour:
            moves.append((self.y + direction, self.x - 1))

            # if it hasn't moved, it can do 2 steps foreward.
            if not self.moved:
                if boxes[self.y + 2 * direction][self.x] is None or boxes[self.y + 2 * direction][self.x]._colour != self._colour:
                    moves.append((self.y + 2 * direction, self.x))

        return moves


class Player:
    pass


class Chess:
    def __init__(self, white: Player, black: Player):
        self.board = Board(8, 8)
        self.resetBoard()

        #white player and black player placeholders (these guys can store their individual pieces maybe)
        self.white = white
        self.black = black

    def move(self, startX, startY, endX, endY):

        # Moves and deletes the piece that was at the landing square (if any)
        self.board._boxes[endY][endX] = self.board._boxes[startY][startX]
        self.board._boxes[startY][startX] = None
        print(f'Moved {self.board._boxes[startY][startX]} to ({endX}, {endY})')

        #Since the pawn just moved, it isn't allowed to move 2 squares again.
        if isinstance(self.board._boxes[endY][endX], Pawn):
            self.board._boxes[endY][endX].moved = True

        # if king.castling(): > logic for moving other pieces is contained within king class? not sure the best way to do this part tbh.

    #test method please ignore
    def printBoard(self):
        for row in self.board._boxes:
            print([type(x) for x in row])

    # cool way of setting it up
    def resetBoard(self):  # ! put this in init method?
        # Pieces and Pawns
        colours = ((0, 1, True), (7, 6, False))
        pieces = (Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)
        for info in colours:
            for i in range(8):
                self.board._boxes[info[0]][i] = pieces[i](info[2], info[0], i)
                self.board._boxes[info[1]][i] = Pawn(info[2],  info[1], i)

        # Empty
        for j in range(2, 6):
            for i in range(8):
                self.board._boxes[j][i] = None

# board = Board()
# board.resetBoard()
# for row in board._boxes:
#     print([type(x) for x in row])


chess = Chess(Player(), Player())
chess.move(0, 0, 0, 2)
chess.printBoard()

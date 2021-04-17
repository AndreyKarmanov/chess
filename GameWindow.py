import pygame
import sys
import os
import time
import random
import chess

WIDTH, HEIGHT = 580, 580
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
COLOURONE, COLOURTWO = (145, 100, 40), (105, 80, 60)
PIECEHEIGHT, PIECEWIDTH = 50, 50
SQUAREWIDTH = int(PIECEWIDTH * 1.2)

dragged = None
draggedMoves = None

translate = {
    chess.Pawn: "Pawn",
    chess.Rook: "Rook",
    chess.Knight: "Knight",
    chess.Bishop: "Bishop",
    chess.King: "King",
    chess.Queen: "Queen"
}

pics = {
    True: {
    },
    False: {
    }
}

for piece in translate.values():
    image = pygame.image.load(os.path.join('Assets', f'White{piece}.png'))
    scaled = pygame.transform.scale(image, (PIECEWIDTH, PIECEHEIGHT))
    pics[True][piece] = scaled

    image = pygame.image.load(os.path.join('Assets', f'Black{piece}.png'))
    scaled = pygame.transform.scale(image, (PIECEWIDTH, PIECEHEIGHT))
    pics[False][piece] = scaled

print(pics)


def getPic(Piece: chess.Pieces, dragged=False):
    if not dragged:
        x = squares[Piece.y][Piece.x].x + (SQUAREWIDTH - PIECEWIDTH) / 2
        y = squares[Piece.y][Piece.x].y + (SQUAREWIDTH - PIECEHEIGHT) / 2
    else:
        x = pygame.mouse.get_pos()[0] - PIECEWIDTH / 2
        y = pygame.mouse.get_pos()[1] - PIECEHEIGHT / 2

    WIN.blit(pics[Piece._colour][translate[type(Piece)]], (x, y))


class Square(pygame.Rect):
    occupied = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pos(self):
        return (self.x, self.y)


def genSquares(x, y, width, height):
    squares = [[] for x in range(height)]
    for rows in range(height):
        for cols in range(width):
            x1 = x + cols * SQUAREWIDTH
            y1 = y + rows * SQUAREWIDTH
            sqr = Square(x1, y1, SQUAREWIDTH, SQUAREWIDTH)
            squares[rows].append(Square(x1, y1, SQUAREWIDTH, SQUAREWIDTH))

    return squares


squares = genSquares(50, 50, 8, 8)


def randomColour():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


c = chess.Chess(chess.Player(), chess.Player())
board = c.getBoard()
for num, row in enumerate(board):
    print([type(x) for x in row], num)


def drawCheckered(x, y, width, height):
    black = pygame.Rect(x, y, SQUAREWIDTH * width, SQUAREWIDTH * height)
    pygame.draw.rect(WIN, COLOURONE, black, 0)

    for rows in range(height):
        colour = rows
        for cols in range(width):
            if colour := (colour + 1) % 2:
                x1 = x + cols * SQUAREWIDTH
                y2 = y + rows * SQUAREWIDTH
                square = pygame.Rect(x1, y2, SQUAREWIDTH, SQUAREWIDTH)
                pygame.draw.rect(WIN, COLOURTWO, square, 0)


def findpiece(mouse):
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if piece and squares[y][x].collidepoint(mouse):
                return piece
    return None


def display():
    WIN.fill((125, 125, 125))
    drawCheckered(50, 50, 8, 8)
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if piece:
                if piece != dragged:
                    getPic(piece)
                else:
                    drawDragged(piece)
                    getPic(piece, True)

    pygame.display.update()


def drawPiece(piece):
    asdf = (0, 0, 0)
    if piece._colour:
        asdf = (225, 225, 225)
    pygame.draw.rect(WIN, asdf, squares[piece.y][piece.x], 5)


def drawDragged(piece):
    asdf = (0, 0, 0)
    if piece._colour:
        asdf = (225, 225, 225)

    for x, y in draggedMoves:
        pygame.draw.rect(WIN, (0, 155, 0), squares[y][x], 0)
    # mouse = pygame.mouse.get_pos()
    # rect = pygame.Rect(mouse[0] - PIECEWIDTH/2, mouse[1] -
    #                    PIECEHEIGHT/2, SQUAREWIDTH, SQUAREWIDTH)
    # pygame.draw.rect(WIN, asdf, rect, 5)


def run():
    global dragged, board, draggedMoves
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if dragged := findpiece(pygame.mouse.get_pos()):
                        print("dragging", dragged.x, dragged.y, type(dragged))
                        draggedMoves = dragged.getMoves(board)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if dragged is not None:
                        if coords := findSquare():
                            if coords in dragged.getMoves(board):
                                c.move(dragged.x, dragged.y,
                                       coords[0], coords[1])
                                board = c.getBoard()
                    dragged = None
        display()


def findSquare():
    for y, row in enumerate(squares):
        for x, square in enumerate(row):
            if squares[y][x].collidepoint(pygame.mouse.get_pos()):
                return (x, y)
    return None


run()

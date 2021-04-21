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


def loadImages():
    for piece in translate.values():
        image = pygame.image.load(os.path.join('Assets', f'White{piece}.png'))
        scaled = pygame.transform.scale(image, (PIECEWIDTH, PIECEHEIGHT))
        pics[True][piece] = scaled

        image = pygame.image.load(os.path.join('Assets', f'Black{piece}.png'))
        scaled = pygame.transform.scale(image, (PIECEWIDTH, PIECEHEIGHT))
        pics[False][piece] = scaled


def genSquares(x, y, width, height):
    squares = [[] for x in range(height)]
    for rows in range(height):
        for cols in range(width):
            x1 = x + cols * SQUAREWIDTH
            y1 = y + rows * SQUAREWIDTH
            squares[rows].append(pygame.Rect(x1, y1, SQUAREWIDTH, SQUAREWIDTH))
    return squares


c = chess.Chess(chess.Player(), chess.Player())
board = c.getBoard()
squares = genSquares(50, 50, 8, 8)
loadImages()


def findpiece(mouse):
    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if piece and squares[y][x].collidepoint(mouse):
                return piece
    return None


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


def getPic(Piece: chess.Pieces, dragged=False):
    if not dragged:
        x = squares[Piece.y][Piece.x].x + (SQUAREWIDTH - PIECEWIDTH) / 2
        y = squares[Piece.y][Piece.x].y + (SQUAREWIDTH - PIECEHEIGHT) / 2
    else:
        mouse = pygame.mouse.get_pos()
        x = mouse[0] - PIECEWIDTH / 2
        y = mouse[1] - PIECEHEIGHT / 2

    WIN.blit(pics[Piece._colour][translate[type(Piece)]], (x, y))


def display():
    WIN.fill((125, 125, 125))
    drawCheckered(50, 50, 8, 8)

    if dragged:
        for x, y in draggedMoves:
            pygame.draw.rect(WIN, (34, 139, 34), squares[y][x], 0)

        getPic(dragged, True)

    for y, row in enumerate(board):
        for x, piece in enumerate(row):
            if piece:
                if piece != dragged:
                    getPic(piece)

    pygame.display.update()


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

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if dragged is not None:
                        if coords := findSquare():
                            if coords in draggedMoves:
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

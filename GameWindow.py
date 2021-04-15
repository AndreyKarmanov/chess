import pygame
import sys
import random
import chess

WIDTH, HEIGHT = 580, 580
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
COLOURONE, COLOURTWO = (145, 100, 40), (105, 80, 60)
PIECEHEIGHT, PIECEWIDTH = 50, 50
SQUAREWIDTH = int(PIECEWIDTH * 1.2)

dragged = None


class Square(pygame.Rect):
    occupied = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def genRandomSquares(num):
    for x in range(num):
        yield pygame.Rect(random.randint(0, WIDTH - PIECEWIDTH), random.randint(0, HEIGHT - PIECEHEIGHT), PIECEHEIGHT,
                          PIECEWIDTH)


def genSquares(x, y, width, height):
    squares = [[] for x in range(height)]
    for rows in range(height):
        for cols in range(width):
            x1 = x + cols * SQUAREWIDTH
            y1 = y + rows * SQUAREWIDTH
            squares[rows].append(Square(x1, y1, SQUAREWIDTH, SQUAREWIDTH))
    return squares


squares = genSquares(50, 50, 8, 8)


def randomColour():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


pieces = [[x, randomColour(), False] for x in list(genRandomSquares(15))]

for x in pieces:
    print(x)


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


def display():
    WIN.fill((125, 125, 125))
    drawCheckered(50, 50, 8, 8)
    for piece, colour, dragged in pieces:
        if not dragged:
            pygame.draw.rect(WIN, colour, piece, 5)
        else:
            x = pygame.Rect(pygame.mouse.get_pos()[0] - PIECEWIDTH / 2, pygame.mouse.get_pos()[1] - PIECEHEIGHT / 2,
                            PIECEHEIGHT, PIECEWIDTH)
            pygame.draw.rect(WIN, colour, x, 5)
    pygame.display.update()


def findpiece(mouse):
    for num, piece in enumerate(pieces):
        if piece[0].collidepoint(mouse):
            return num
    return None


def displayMoves(piece):
    pass


def run():
    global dragged
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if findpiece(pygame.mouse.get_pos()) is not None:
                        dragged = findpiece(pygame.mouse.get_pos())
                        pieces[dragged][2] = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if dragged is not None:
                        for num, rows in enumerate(squares):
                            for square in rows:
                                if not square.occupied and square.collidepoint(pygame.mouse.get_pos()):
                                    pieces[dragged][0].x = square.x + (SQUAREWIDTH - PIECEWIDTH) / 2
                                    pieces[dragged][0].y = square.y + (SQUAREWIDTH - PIECEHEIGHT) / 2
                                    square.occupied = True

                        pieces[dragged][2] = False
                        dragged = None

        display()

run()

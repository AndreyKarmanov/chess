import pygame
import sys
import random

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
PEICEHEIGHT, PEICEWIDTH = 50, 50
dragged = None


def genSquares(num):
    for x in range(num):
        yield pygame.Rect(random.randint(0, WIDTH - PEICEWIDTH), random.randint(0, HEIGHT - PEICEWIDTH), PEICEHEIGHT,
                          PEICEWIDTH)


def randomColour():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


peices = [[x, randomColour(), False] for x in list(genSquares(15))]


def display():
    WIN.fill((125, 125, 125))
    for peice, colour, dragged in peices:
        if not dragged:
            pygame.draw.rect(WIN, colour, peice, 5)
        else:
            x = pygame.Rect(pygame.mouse.get_pos()[0] - PEICEWIDTH / 2, pygame.mouse.get_pos()[1] - PEICEHEIGHT / 2,
                            PEICEHEIGHT, PEICEWIDTH)
            pygame.draw.rect(WIN, colour, x, 5)
    pygame.display.update()


def findPeice(mouse):
    for num, peice in enumerate(peices):
        if peice[0].collidepoint(mouse):
            return num
    return None


def displayMoves(peice):
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
                    print(findPeice(pygame.mouse.get_pos()))
                    if findPeice(pygame.mouse.get_pos()) is not None:
                        dragged = findPeice(pygame.mouse.get_pos())
                        peices[dragged][2] = True
                        print(peices[dragged])

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    print(dragged)
                    if dragged is not None:
                        peices[dragged][0].x = pygame.mouse.get_pos()[
                            0] - PEICEWIDTH / 2
                        peices[dragged][0].y = pygame.mouse.get_pos()[
                            1] - PEICEHEIGHT / 2
                        peices[dragged][2] = False
                        dragged = None

        display()
run()
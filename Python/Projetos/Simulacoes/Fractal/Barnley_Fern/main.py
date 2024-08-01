import pygame
from pygame.locals import *
from Pygame import *
from random import random

pygame.init()

LARGURA, ALTURA = 1700, 1000

x, y = 0, 0

janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Barnsley Fern")

clock = pygame.time.Clock()


def novoPonto():
    global x, y
    r = random()

    if r < 0.01:
        x_novo = 0
        y_novo = 0.16 * y
    elif r < 0.86:
        # 2
        x_novo = 0.85 * x + 0.04 * y
        y_novo = -0.04 * x + 0.85 * y + 1.6
    elif r < 0.93:
        # 3
        x_novo = 0.2 * x + -0.26 * y
        y_novo = 0.23 * x + 0.22 * y + 1.6
    else:
        # 4
        x_novo = -0.15 * x + 0.28 * y
        y_novo = 0.26 * x + 0.24 * y + 0.44

    x = x_novo
    y = y_novo


def desenharPonto():
    px = map_valor(x, -2.1820, 2.6558, 0, LARGURA)
    py = map_valor(y, 0, 9.9983, ALTURA, 0)
    ponto(janela, px, py, r=1)


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            exit()

    for i in range(1000):
        desenharPonto()
        novoPonto()

    pygame.display.flip()

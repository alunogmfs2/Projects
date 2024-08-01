import pygame
from pygame.locals import *


def ponto(win, x, y, color="white", r=5):
    pygame.draw.circle(win, color, (x, y), r)


def map_valor(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

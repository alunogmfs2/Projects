import pygame
from pygame.locals import *
import numpy as np
from math import cos, sin

pygame.init()

LARGURA, ALTURA = 800, 600

win = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Rosquinha rotativa')

scala = 100

angle = 90

projecao2dmatrix = np.matrix([[1, 0, 0],
                              [0, 1, 0]])

clock = pygame.time.Clock()

novoPontos = []

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
    #win.fill((0, 0, 0))
    matrixRotacaoZ = np.matrix([[cos(angle), -sin(angle), 0],
                                [sin(angle),  cos(angle), 0],
                                [0,                    0, 1]])
    
    coordenadas = np.matrix([200, 200, 0])
    
    #pygame.draw.circle(win, (255, 255, 255), (coordenadas[0][0], coordenadas[0][1]), 20)
    
    
    for i in range(100):
        for j in range(20):
            
            matrixRotacaoX = np.matrix([[1, 0         , 0],
                            [0, cos(angle), -sin(angle)],
                            [0, sin(angle), cos(angle)]])

            matrixRotacaoY = np.matrix([[cos(angle),  0, sin(angle)],
                            [0,           1, 0],
                            [-sin(angle), 0, cos(angle)]])
            
            rotacaoy = np.dot(matrixRotacaoY, coordenadas.reshape((3, 1)))
            rotacaox = np.dot(matrixRotacaoX, rotacaoy)
            projecao2d = np.dot(projecao2dmatrix, rotacaox)
            
            x = int(projecao2d[0][0]) + LARGURA / 2
            y = int(projecao2d[1][0]) + ALTURA / 2
            
            novoPontos.append([x, y])
            
            angle += 0.00001
        
        #pygame.draw.circle(win, (255, 255, 255), (x, y), 20)
    
    for circulo in novoPontos:
        pygame.draw.circle(win, (255, 255, 255), circulo, 15)
    
    pygame.display.flip()

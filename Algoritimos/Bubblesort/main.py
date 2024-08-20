import pygame
import random

LARGURA, ALTURA = 600, 600

win = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Bubble Sort")

clock = pygame.time.Clock()

barras = list()

def criarBarras():
    global barras
    barras = list(range(1, ALTURA + 1))

def embaralharBarras():
    global barras
    random.shuffle(barras)

def desenharBarras():
    global barras
    win.fill((0, 0, 0))  # Limpa a tela antes de desenhar
    largura_barra = LARGURA // len(barras)
    for i, altura in enumerate(barras):
        pygame.draw.rect(win, (255, 255, 255), (i * largura_barra, ALTURA - altura, largura_barra, altura))
    pygame.display.update()

def bubbleSortGenerator():
    global barras
    n = len(barras)
    for i in range(n):
        for j in range(0, n-i-1):
            if barras[j] > barras[j+1]:
                # Troca os elementos
                barras[j], barras[j+1] = barras[j+1], barras[j]
                yield True  # Pausa a execução para permitir a renderização

criarBarras()
embaralharBarras()

# Inicializa o gerador do Bubble Sort
bubble_sort_gen = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_SPACE:
                if bubble_sort_gen is None:  # Apenas inicializa o gerador se ele não estiver ativo
                    bubble_sort_gen = bubbleSortGenerator()

    if bubble_sort_gen:
        try:
            next(bubble_sort_gen)
        except StopIteration:
            bubble_sort_gen = None  # Reinicia o gerador quando terminar

    desenharBarras()

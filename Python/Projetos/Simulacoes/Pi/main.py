import pygame
from pygame.locals import *

pygame.init()

# Constantes
LARGURA = 800
ALTURA = 600

# Cores
CINZA_ESCURO = (60, 60, 60)
CINZA_CLARO = (192, 192, 192)
AZUL_CLARO = (100, 149, 237)
AZUL_ESCURO = (25, 25, 112)

MASSAQP = 1
MASSAQG = 1

PACOS = 1000000

DIGITOS = 7

# Variaveis de Tamanho
ybuff = 100

lqp = 20
aqp = 20

lc = LARGURA
ac = ALTURA / 2 - ybuff

lqg = 150
aqg = 150

# Variaveis de Posicao
xqp = 100
yqp = ALTURA / 2 + (ybuff - aqp)

xc = 0
yc = ALTURA / 2 + ybuff

xqg = 200
yqg = ALTURA / 2 + (ybuff - aqg)

# Variaveis de Velocidade
vqg = -2 / PACOS
vqp = 0

if DIGITOS == 1:
    DIGITOS = 0
elif DIGITOS > 1:
    pass
else:
    pygame.quit()
    exit()

# Tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Calculando PI')

text = ''

font = pygame.font.SysFont('Arial', 24)

# Clock
clock = pygame.time.Clock()

# Outras Variaveis
contador = 0

class Bloco:
    def __init__(self, x, y, cor, l, a, v, m, cx):
        self.x = x
        self.y = y
        self.cor = cor
        self.l = l
        self.a = a
        self.v = v
        self.m = m
        self.cx = cx

    def colidiu(self, outro):
        global contador
        if not(self.x + self.l < outro.x or self.x > outro.x + outro.l):
            contador += 1
        return not(self.x + self.l < outro.x or self.x > outro.x + outro.l)
    
    def colidiu_parede(self):
        global contador
        if self.x <= 0:
            self.v *= -1
            contador += 1

    def mover(self):
        self.x += self.v

    def quicar(self, outro):
        somaM = self.m + outro.m
        subM = self.m - outro.m

        # No caso unidimensional, as velocidades são valores escalares
        v1f = ((self.m - outro.m) / somaM) * self.v + ((2 * outro.m) / somaM) * outro.v
        v2f = ((2 * self.m) / somaM) * self.v + ((outro.m - self.m) / somaM) * outro.v

        return [v1f, v2f]
    
    def desenhar(self):
        x = constrain(self.x, self.cx, LARGURA)
        pygame.draw.rect(tela, self.cor, (x, self.y, self.l, self.a))

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


def constrain(n, b, a):
    return max(b, min(n, a))

qp = Bloco(xqp, yqp, AZUL_CLARO, lqp, aqp, vqp, 1, 0)
qg = Bloco(xqg, yqg, AZUL_ESCURO, lqg, aqg, vqg, 100**DIGITOS, lqp)


# Loop principal
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    # Atualizar
    for i in range(PACOS):
        if qg.colidiu(qp):
            v = qg.quicar(qp)
            v1 = v[0]
            v2 = v[1]
            qg.v = v1
            qp.v = v2

        qg.colidiu_parede()
        qp.colidiu_parede()

        qg.mover()
        qp.mover()

    text = str(contador)
    text_font = font.render(text, True, (0, 0, 0))
    # Desenhar
    tela.fill(CINZA_CLARO)

    chao = pygame.draw.rect(tela, CINZA_ESCURO, (xc, yc, lc, ac))
    
    qp.desenhar()
    qg.desenhar()

    tela.blit(text_font, (100, 500))
    pygame.display.flip()

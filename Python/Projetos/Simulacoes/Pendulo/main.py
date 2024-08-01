import pygame
from pygame.locals import *
import math

pygame.init()

LARGURA, ALTURA = 600, 400

win = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulacao do Pendulo")

clock = pygame.time.Clock()

class Pendulo:
    def __init__(self):
        self.x_l = LARGURA / 2
        self.y_l = ALTURA / 2
        
        self.r = 100
        self.angulo = -45
        self.angulo_r = self.angulo * math.pi / 180
        self.omega = 0
        self.omega_a = self.omega
        self.G = 9.81
        self.a = self.G * self.r
        self.T = 2 * math.pi * math.sqrt(self.r / self.G)
        self.t = 0        
    def desenhar(self):
        pygame.draw.circle(win, (64, 64, 64), (self.x_l, self.y_l), 5)
        pygame.draw.line(win, (64, 64, 64), (self.x_l, self.y_l), self.calcular_xy(), 3)
        pygame.draw.circle(win, (64, 64, 64), (self.calcular_xy()), 5)
        
    def calcular_xy(self):
        return (self.x_l + math.sin(self.angulo_r) * self.r, self.y_l + math.cos(self.angulo_r) * self.r)
    
    def calcular_ac_a(self):
        self.a = self.G * math.sin(self.angulo_r)
    
    def atualizar_t(self):
        self.t += 0.01
    
    def calcular_omega(self):
        self.omega_a = self.omega_a + self.a * self.t
        
    def atualizar_angulo(self):
        self.angulo_r = self.angulo_r + self.omega_a * self.t + self.a / 2 * self.t ** 2
    
    def update(self):
        self.atualizar_t()
        self.calcular_ac_a()
        self.calcular_omega()
        self.atualizar_angulo()
        if self.t == self.T / 2:
            print(f"\n Mudou \n")
            self.a = -self.a
        
        print(f"Angulo: {self.angulo_r}\nAc. angular: {self.a}\nPeriodo: {self.T}\n")
pendulo = Pendulo()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
            exit()
            
    win.fill((128, 128, 128))
    
    pendulo.update()
    
    pendulo.desenhar()
    
    pygame.display.flip()

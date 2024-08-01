import pygame
from pygame.locals import *
import math

pygame.init()

LARGURA, ALTURA = 600, 400

win = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Simulação do Pêndulo")

clock = pygame.time.Clock()

class Pendulo:
    def __init__(self):
        self.x_l = LARGURA / 2
        self.y_l = ALTURA / 2 - 100
        
        self.r = 250
        self.angulo = 90
        self.angulo_r = math.radians(self.angulo)
        self.omega = 0
        self.G = 9.81
        self.a = 0
        
    def desenhar(self):
        pygame.draw.circle(win, (64, 64, 64), (int(self.x_l), int(self.y_l)), 5)
        pygame.draw.line(win, (64, 64, 64), (self.x_l, self.y_l), self.calcular_xy(), 3)
        pygame.draw.circle(win, (64, 64, 64), (self.calcular_xy()), 5)
        
    def calcular_xy(self):
        return (int(self.x_l + math.sin(self.angulo_r) * self.r), int(self.y_l + math.cos(self.angulo_r) * self.r))
    
    def calcular_ac_a(self):
        self.a = -(self.G / self.r) * math.sin(self.angulo_r)
    
    def calcular_omega(self, dt):
        self.omega += self.a * dt
        
    def atualizar_angulo(self, dt):
        self.angulo_r += self.omega * dt
    
    def update(self, dt):
        self.calcular_ac_a()
        self.calcular_omega(dt)
        self.atualizar_angulo(dt)
        
        print(f"Angulo: {math.degrees(self.angulo_r):.5f}\nAc. angular: {self.a:.5f}\nVel. angular: {self.omega:.5f}\n")

pendulo = Pendulo()

while True:
    dt = clock.tick(60) / 1000  # 60 FPS, convert ms to s
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
    
    win.fill((128, 128, 128))
    
    pendulo.update(dt)
    
    pendulo.desenhar()
    
    pygame.display.flip()

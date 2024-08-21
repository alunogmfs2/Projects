import pygame
from pygame.locals import *

WIDTH, HEIGHT = 1000, 600

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 100
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.velocityX = 5
        self.velocityY = 5
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getRadius(self):
        return self.radius
    
    def update(self, other: Player):
        self.x += self.velocityX
        self.y += self.velocityY
        
        if self.x + self.radius >= WIDTH or self.x - self.radius <= 0:
            self.velocityX = -self.velocityX
        
        if self.y + self.radius >= HEIGHT or self.y - self.radius <= 0:
            self.velocityY = -self.velocityY

        if self.x + self.radius >= other.getX() and (self.y + self.radius >= other.getY() and self.y - self.radius >= other.getY() + other.height):
            self.velocityX = -self.velocityX

player1 = Player(10, HEIGHT / 2 - 50)
player2 = Player(WIDTH - 25, HEIGHT / 2 - 50)
ball = Ball(WIDTH / 2, HEIGHT / 2)

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
            if event.key == K_w:
                player1.y -= 20
                
            if event.key == K_s:
                player1.y += 20
                
            if event.key == K_UP:
                player2.y -= 20
                
            if event.key == K_DOWN:
                player2.y += 20
    
    win.fill((0, 0, 0))
    
    ball.update(player2)
    
    pygame.draw.rect(win, (255, 255, 255), (player1.getX(), player1.getY(), player1.getWidth(), player1.getHeight()))
    pygame.draw.rect(win, (255, 255, 255), (player2.getX(), player2.getY(), player2.getWidth(), player2.getHeight()))
    
    pygame.draw.circle(win, (255, 255, 255), (ball.getX(), ball.getY()), ball.getRadius())
    
    pygame.display.flip()

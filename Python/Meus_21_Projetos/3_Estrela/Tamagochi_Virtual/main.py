import pygame
from pygame.locals import *

LARGURA, ALTURA = 800, 600

tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.display.set_caption("Tamagochi Virtual")

clock = pygame.time.Clock()

sprite_sheet = pygame.image.load("E:\\Programacao\\Projetos\\Projects\\Python\\Meus_21_Projetos\\3_Estrela\\Tamagochi_Virtual\\tamgotchi.png")

class Tamagotchi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.x, self.y = LARGURA / 2, ALTURA / 2 + 250

        self.imagens_tamagotchi = []
        
        self.img = sprite_sheet.subsurface((0, 0), (32, 32))
        self.img = pygame.transform.scale(self.img, (32 * 6, 32 * 6))
        self.img2 = sprite_sheet.subsurface((96, 0), (32, 32))
        self.img2 = pygame.transform.scale(self.img2, (32 * 6, 32 * 6))
        self.img3 = sprite_sheet.subsurface((64, 0), (32, 32))
        self.img3 = pygame.transform.scale(self.img3, (32 * 6, 32 * 6))
        self.img4 = sprite_sheet.subsurface((32, 0), (32, 32))
        self.img4 = pygame.transform.scale(self.img4, (32 * 6, 32 * 6))

        self.imagens_tamagotchi.append(self.img)
        self.imagens_tamagotchi.append(self.img2)
        self.imagens_tamagotchi.append(self.img3)
        self.imagens_tamagotchi.append(self.img4)

        self.index_lista = 0
        self.image = self.imagens_tamagotchi[0]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update_sprite(self):
        self.index_lista += 0.01
        if self.index_lista > 4:
            self.index_lista = 0
        self.image = self.imagens_tamagotchi[int(self.index_lista)]

    def update(self):
        self.update_sprite()

todas_as_sprites = pygame.sprite.Group()
tamagotchi = Tamagotchi()
todas_as_sprites.add(tamagotchi)

while True:
    clock.tick(60)
    tela.fill("white")
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
    
    todas_as_sprites.update()
    todas_as_sprites.draw(tela)

    pygame.display.flip()


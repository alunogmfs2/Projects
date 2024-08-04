from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from noise import snoise2
import random

app = Ursina()

# Configurações iniciais
window.title = 'Minecraft Clone'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# Definindo o nível do chão e as dimensões do terreno
GROUND_LEVEL = 0
WIDTH = 50
DEPTH = 50
SCALE = 20
HEIGHT = 10
CAVE_CHANCE = 0.1  # Probabilidade de uma célula ser uma caverna

# Função para gerar terreno com cavernas usando Perlin Noise
def generate_terrain_with_caves(width, depth, scale, height):
    for z in range(depth):
        for x in range(width):
            # Usar snoise2 para gerar a altura dos voxels
            y = int(snoise2(x / scale, z / scale, octaves=4) * height)
            
            # Verificar se o ponto deve ser uma caverna
            if random.random() < CAVE_CHANCE:
                continue
            
            # Gerar cubos somente se a altura for positiva
            for h in range(GROUND_LEVEL, GROUND_LEVEL + y):
                voxel = Voxel(position=(x, h, z))

# Crie uma entidade de voxel
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture='white_cube',
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.lime,
        )
        self.collider = 'box'

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                # Adicionar um voxel na direção do mouse
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                # Remover o voxel atual
                destroy(self)

# Crie uma entidade de chão que cobre toda a área
class Ground(Entity):
    def __init__(self, width, depth, **kwargs):
        super().__init__(
            parent=scene,
            model='plane',  # Use 'plane' para criar um plano
            texture='grass',
            color=color.green,
            scale=(width / 10, 1, depth / 10),  # Ajuste a escala para o tamanho do chão
            position=(width / 2, GROUND_LEVEL, depth / 2),
            **kwargs
        )
        self.collider = 'box'

# Gere a área de terreno com cavernas
generate_terrain_with_caves(width=WIDTH, depth=DEPTH, scale=SCALE, height=HEIGHT)

# Adicione um chão básico
ground = Ground(WIDTH, DEPTH)

# Adicione o controlador de primeira pessoa
player = FirstPersonController()
player.position = (WIDTH / 2, HEIGHT / 2, DEPTH / 2)  # Ajuste a posição inicial do jogador

app.run()

import pygame as pg
import numpy as np
from math import * #type:ignore

import pygame.display

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

pg.init()
WIDTH, HEIGHT = 800, 600
pygame.display.set_caption("3D Cube")
win = pygame.display.set_mode((800, 600))

scale = 100

circle_pos = [WIDTH / 2, HEIGHT / 2]

angle = 0

points = list()

points.append(np.matrix([[-1], [-1], [1]]))
points.append(np.matrix([[1], [-1], [1]]))
points.append(np.matrix([[1], [1], [1]]))
points.append(np.matrix([[-1], [1], [1]]))
points.append(np.matrix([[-1], [-1], [-1]]))
points.append(np.matrix([[1], [-1], [-1]]))
points.append(np.matrix([[1], [1], [-1]]))
points.append(np.matrix([[-1], [1], [-1]]))



projection_matrix = np.matrix([
    [1, 0, 0],
    [0, 1, 0]
])

projected_points = [
    [n, n] for n in range(len(points))
]


def connectPoints(i, j, points):
    pygame.draw.line(win, (WHITE), (points[i][0], points[i][1]), (points[j][0], points[j][1]))


clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    # Update

    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])

    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)],
    ])

    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)],
    ])

    angle += 0.015

    # Draw
    win.fill(BLACK)

    i = 0
    for point in points:
        rotated2d = np.dot(rotation_z, point.reshape((3, 1)))
        rotated2d = np.dot(rotation_y, rotated2d)
        rotated2d = np.dot(rotation_x, rotated2d)

        projected2d = np.dot(projection_matrix, rotated2d)

        x = int(projected2d[0][0] * scale) + circle_pos[0]
        y = int(projected2d[1][0] * scale) + circle_pos[1]
        projected_points[i] = [x, y] #type: ignore
        pygame.draw.circle(win, WHITE, (x, y), 7)
        i += 1

    connectPoints(0, 1, projected_points)
    connectPoints(1, 2, projected_points)
    connectPoints(2, 3, projected_points)
    connectPoints(3, 0, projected_points)
    connectPoints(0, 4, projected_points)
    connectPoints(4, 5, projected_points)
    connectPoints(5, 1, projected_points)
    connectPoints(5, 6, projected_points)
    connectPoints(6, 2, projected_points)
    connectPoints(6, 7, projected_points)
    connectPoints(7, 3, projected_points)
    connectPoints(7, 4, projected_points)

    pygame.display.flip()

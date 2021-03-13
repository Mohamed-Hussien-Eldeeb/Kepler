from math import *
import numpy as np
import pygame


def position(e, T, r_0):
    E = 0
    out = []
    acc = 1 / T
    for t in np.arange(0, T, acc):
        M = 2 * pi * t / T
        E -= (E - e * sin(E) - M) / (1 - e * cos(E))
        V = 2 * atan(sqrt((1 + e) / (1 - e)) * tan(E / 2))
        r = r_0 * (1 - e ** 2) / (1 + e * cos(V))
        out.append([r, V])
    return out


running = True
pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Kepler')
clock = pygame.time.Clock()
pos = 0
ro = 0
font = pygame.font.Font('freesansbold.ttf', 20)
while running:
    window.fill('black')
    text = font.render(f'e = {round(ro, 2)}', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (200, 800)
    window.blit(text, textRect)
    motion = position(ro, 10, 250)
    for i in motion:
        pygame.draw.circle(window, 'white', [i[0] * cos(i[1]) + 500, i[0] * sin(i[1]) + 500], 1)
    pygame.draw.circle(window, 'blue',
                       [motion[pos][0] * cos(motion[pos][1]) + 500, motion[pos][0] * sin(motion[pos][1]) + 500],
                       15)
    pygame.draw.circle(window, 'orange', [500, 500], 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(60)
    pos += 1
    pos %= len(motion)
    ro += 0.0005
    ro %= 0.8
pygame.quit()
quit()

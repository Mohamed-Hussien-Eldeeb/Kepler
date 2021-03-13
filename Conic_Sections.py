from math import *
import numpy as np
import pygame

running = True
pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Conic Sections')
clock = pygame.time.Clock()
e = 0
font = pygame.font.Font('freesansbold.ttf', 20)
while running:
    window.fill('black')
    text = font.render(f'e = {round(e, 1)}', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (200, 800)
    window.blit(text, textRect)
    for theta in np.arange(0, 2 * pi, 2 * pi / 1440):
        r = 100 * (1 - e ** 2) / (1 + e * cos(theta))
        pygame.draw.circle(window, 'white', [r * cos(theta) + 500 + e * 100, r * sin(theta) + 500], 2)
    pygame.draw.circle(window, 'white', [500 - e * 100, 500], 5)
    pygame.draw.circle(window, 'white', [500 + e * 100, 500], 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(120)
    e += 0.005
    e %= 5
pygame.quit()
quit()

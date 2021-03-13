from math import *
import numpy as np
import pygame

G = 6.67408 * 10 ** -11 / 100000000000000


class Planet:
    def __init__(self, mass, position, radius, velocity, color):
        self.mass = mass
        self.position = np.array(position, dtype='float32')
        self.radius = radius
        self.velocity = np.array(velocity, dtype='float32')
        self.color = color
        self.trails = []

    def move(self, time):
        s = self.position - sun.position
        d = np.linalg.norm(s)
        if d == 0:
            d = 1
        ra = s / d
        a = G * sun.mass * ra / d ** 2
        self.velocity -= a * time
        self.position += self.velocity * time
        self.trails.append(tuple(self.position))
        if len(self.trails) > 200:
            self.trails = self.trails[1:]

    def draw(self):
        for i in self.trails:
            pygame.draw.circle(window, 'white', [i[0] + 500, i[1] + 500], 1)
        pygame.draw.circle(window, self.color, self.position + 500, self.radius)


scale_r = 15
scale_d = 200

sun = Planet(1.989 * 10 ** 30, [0, 0], 3 * scale_r, [0, 0], 'orange')
mercury = Planet(3.285 * 10 ** 23, [0.387 * scale_d, 0], 0.383 * scale_r, [0, 140], 'white')
venus = Planet(4.867 * 10 ** 24, [0.723 * scale_d, 0], 0.949 * scale_r, [0, 100], (139, 125, 130))
earth = Planet(5.972 * 10 ** 24, [scale_d, 0], scale_r, [0, 90], 'blue')
mars = Planet(6.39 * 10 ** 23, [1.52 * scale_d, 0], 0.532 * scale_r, [0, 70], 'red')
running = True
pygame.init()
window = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Kepler')
clock = pygame.time.Clock()
theta = 0
while running:
    window.fill('black')
    sun.draw()
    mercury.draw()
    venus.draw()
    earth.draw()
    mars.draw()
    mercury.move(1 / (0.240846 * 30))
    venus.move(1 / (0.615 * 30))
    earth.move(1 / (1 * 30))
    mars.move(1 / (1.881 * 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(360)
pygame.quit()
quit()

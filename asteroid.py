import pygame.draw
from pygame.examples.scrap_clipboard import screen

from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        pygame.draw.circle(screen, "white", (self.x / 2) + self.radius, self.radius, 2)
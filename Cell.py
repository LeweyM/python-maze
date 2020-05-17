import pygame


class Cell:

    def __init__(self, surface, x, y, width):
        self.width = width
        self.x = x
        self.y = y
        self.surface = surface

    def show(self):
        pygame.draw.rect(
            self.surface, pygame.Color("white"),
            (self.x * self.width, self.y * self.width, self.width, self.width))

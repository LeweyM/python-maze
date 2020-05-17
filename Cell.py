import pygame


class Cell:

    def __init__(self, surface, x, y, width):
        self.width = width
        self.x = x
        self.y = y
        self.surface = surface

    def show(self):
        white = pygame.Color("white")
        # top
        pygame.draw.line(self.surface, white,
                         (self.x * self.width, self.y * self.width),
                         (self.x * self.width + self.width, self.y * self.width))

        # left
        pygame.draw.line(self.surface, white,
                         (self.x * self.width, self.y * self.width),
                         (self.x * self.width, self.y * self.width + self.width))

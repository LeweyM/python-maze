import pygame


class Cell:

    def __init__(self, surface, x, y, width):
        self.width = width
        self.x = x
        self.y = y
        self.surface = surface
        self.top = True
        self.left = True

    def __str__(self):
        return f"(%s, %s)" % (self.x, self.y)

    def show_red(self):
        red = pygame.Color("red")
        pygame.draw.rect(self.surface, red, (self.x * self.width, self.y * self.width, self.width, self.width))

    def show(self):
        white = pygame.Color("white")
        # top
        self.show_lines(white)

    def show_lines(self, color):
        if self.top:
            pygame.draw.line(self.surface, color,
                             (self.x * self.width, self.y * self.width),
                             (self.x * self.width + self.width, self.y * self.width))
        # left
        if self.left:
            pygame.draw.line(self.surface, color,
                             (self.x * self.width, self.y * self.width),
                             (self.x * self.width, self.y * self.width + self.width))

    def open(self, other):
        if self.y > other.y and self.x == other.x:
            self.top = False
        if other.y > self.y and self.x == other.x:
            other.top = False
        if self.x > other.x and self.y == other.y:
            self.left = False
        if other.x > self.x and self.y == other.y:
            other.left = False

    def get_neighbor_indicies(self):
        return [
            (self.x + 1, self.y),
            (self.x - 1, self.y),
            (self.x, self.y + 1),
            (self.x, self.y - 1),
        ]

    def open_between(self, other):
        pass

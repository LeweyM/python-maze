import pygame

from Grid import Grid
from Solver import Solver

pygame.init()

res = 100
size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

grid = Grid(width, res, screen)
while not grid.finished():
    grid.update()

solver = Solver(grid)
crashed = False

while not crashed:
    screen.fill((0, 0, 0))

    # pygame.time.delay(1000)

    grid.show_trail(solver.solve())
    grid.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.flip()
    clock.tick(60)

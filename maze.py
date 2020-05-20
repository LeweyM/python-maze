import pygame

from Grid import Grid
from Solver import Solver

pygame.init()

res = 20
size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

grid = Grid(width, res, screen)
solver = Solver(grid)

crashed = False

while not crashed:
    screen.fill((0, 0, 0))

    grid.update()

    if grid.finished():
        solver.update()
        solver.show_visited_nodes()

        if solver.finished:
            solver.show_trail()
            grid.show()
            pygame.display.flip()
            pygame.time.delay(3000)
            grid = Grid(width, res, screen)
            solver = Solver(grid)
    grid.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.flip()
    clock.tick(60)

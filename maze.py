import pygame

from Cell import Cell

res = 10

pygame.init()

size = width, height = 320, 320
speed = [2, 2]
black = 0, 0, 0

cell_width = width // res

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

grid = []

for x in range(res):
    for y in range(res):
        grid.append(Cell(screen, x, y, cell_width))

print(grid)

crashed = False

while not crashed:

    for cell in grid:
        cell.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()
    clock.tick(60)

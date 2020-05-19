import pygame

from Grid import Grid

pygame.init()

res = 20
size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

grid = Grid(width, res, screen)
while not grid.finished():
    grid.update()

pygame.display.flip()
screen.fill((0, 0, 0))
grid.show()
pygame.display.flip()

grid.solve()
crashed = False

while not crashed:
    screen.fill((0, 0, 0))

    # pygame.time.delay(1000)

    grid.show_trail()
    grid.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.flip()
    clock.tick(60)

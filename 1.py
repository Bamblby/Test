import pygame
from random import randrange


LB = 300
LV = 50

x, y = randrange(0, LB, LV), randrange(0, LB, LV)
apple = randrange(0, LB, LV), randrange(0, LB, LV)
lenght = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 3

pygame.init()
sc = pygame.display.set_mode([LB, LB])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))

    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, LV - 3, LV - 3))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, LV, LV))

    x += dx * LV
    y += dy * LV
    snake.append((x, y))
    snake = snake[-lenght:]

    if snake[-1] == apple:
        apple = randrange(0, LB, LV), randrange(0, LB, LV)
        lenght += 1
        fps += 1

        if x < 0 or x > LB - LV or y < 0 or y > LB - LV or len(snake) != len(set(snake)):
            break
        if len(snake) != len(set(snake)):
            break
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1

    if key[pygame.K_s]:
        dx, dy = 0, 1

    if key[pygame.K_a]:
        dx, dy = -1, 0

    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
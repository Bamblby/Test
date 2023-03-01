import pygame
from random import randrange

LB = 800
LV = 50

x, y = randrange(0, LB, LV), randrange(0, LB, LV)
apple = randrange(0, LB, LV), randrange(0, LB, LV)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
lenght = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([LB, LB])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 26, bold=True)

while True:
    sc.fill(pygame.Color('black'))

    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, LV - 2, LV - 2))) for i, j in snake]
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
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}

    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}

    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}

    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
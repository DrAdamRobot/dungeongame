import pygame
import constants
from character import Character
pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("dungeon game")
moving_left = False
moving_right = False
moving_up = False
moving_down = False
player = Character(100, 100)
run = True
while run:
    dx = 0
    dy = 0
    if moving_right == True:
        dx = 5
    if moving_left == True:
        dx = -5
    if moving_up == True:
        dy = -5
    if moving_down == True:
        dy = 5

    player.move(dx, dy)

    player.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_s:
                moving_down = True



    pygame.display.update()

pygame.QUIT
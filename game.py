import pygame
import sys
from monster import Enemy

clock = pygame.time.Clock()
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

moving_sprites = pygame.sprite.Group()
enemy = Enemy(200, 200)
moving_sprites.add(enemy)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                enemy.action = 0
                enemy.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                enemy.action == 4
                enemy.update()
                
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    clock.tick(60)

    pygame.display.update()
import pygame
from gamesprites import *
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 500)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud(SCREEN_WIDTH, SCREEN_HEIGHT)
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)

    #  Get the keys pressed
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()
    clouds.update()

    # Fill the background with white
    screen.fill((135, 206, 250))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        # If so, remove the player and stop the loop
        player.kill()
        running = False

    # Contents of the game surfaced pushed to the display.
    pygame.display.flip()
    clock.tick(30)  # Lock at 30fps

pygame.quit()
# https://realpython.com/pygame-a-primer/

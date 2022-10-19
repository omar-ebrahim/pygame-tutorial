import random
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    RLEACCEL
)


class Player(pygame.sprite.Sprite):  # The player class inherits the Sprite class
    def __init__(self, screen_width, screen_height) -> None:
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        elif pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        elif pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Collision detection
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Enemy, self).__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.screen_width + 20,
                               self.screen_width + 100),
                random.randint(0, self.screen_height),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove it when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Cloud, self).__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surf = pygame.image.load("cloud.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(self.screen_width + 20,
                               self.screen_width + 100),
                random.randint(0, self.screen_height),
            )
        )
    
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
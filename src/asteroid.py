import pygame
import random
from .config import ASTEROID_SPEED

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/asteroid.png").convert_alpha()
        self.rect = self.image.get_rect(
            center=(random.randint(50, 750), -50)
        )

    def update(self):
        self.rect.y += ASTEROID_SPEED
        if self.rect.top > 600:
            self.kill()


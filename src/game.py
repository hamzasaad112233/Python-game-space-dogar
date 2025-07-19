import pygame
import random
from .player import Player
from .asteroid import Asteroid
from .config import WIDTH, HEIGHT, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Dodger")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("assets/background.png").convert()
        self.running = True

        self.player = Player(WIDTH // 2, HEIGHT - 60)
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.asteroids = pygame.sprite.Group()
        self.spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawn_event, 1000)

        self.score = 0
        self.font = pygame.font.SysFont("Arial", 28)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == self.spawn_event:
                self.asteroids.add(Asteroid())

    def update(self):
        keys = pygame.key.get_pressed()
        self.player_group.update(keys)
        self.asteroids.update()

        if pygame.sprite.spritecollide(self.player, self.asteroids, False):
            self.running = False

        self.score += 1

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player_group.draw(self.screen)
        self.asteroids.draw(self.screen)
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()


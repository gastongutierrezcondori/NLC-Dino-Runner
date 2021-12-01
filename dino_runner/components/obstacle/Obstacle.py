import self as self
from pygame.sprite import Sprite

from utils.constants import SCREEN_WIDTH


class Obstacle(Sprite):



    def __init__(self, Image, type):
        self.image = Image
        self.type = type
        self.rect = self.image[type].get_rect()
        self.rect.x = SCREEN_WIDTH


    def update(self, game_speed, obstacles: list):
        self.rect.x -= game_speed
        self.rect.y = 320

        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)

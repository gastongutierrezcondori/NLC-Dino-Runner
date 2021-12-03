import pygame

from utils.constants import HEART, LIST_LIVES
from pygame.sprite import Sprite

class Lives(Sprite):
    X_POS = 900
    Y_POS = 20
    def __init__(self):
        self.Image = HEART
        self.rect = self.Image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.lives = LIST_LIVES

    def update(self, game):
        print(game.lives)
        if game.lives > 0:
            game.lives -= 1
            self.take_life(game.lives, game)
        else:
            pygame.time.delay(500)
            game.playing = False
            game.death_count += 1
            game.points = 0

    def draw(self, screen, game):
        for live in game.live_list:
            self.rect.x = live
            screen.blit(self.Image, (self.rect.x, self.rect.y))

    def take_life(self, position, game):
        if len(game.live_list) != 0:
            game.live_list.pop(position)

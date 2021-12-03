import pygame

from components.lives import Lives
from components.obstacle.Cactus import Cactus
from utils.constants import SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    Lives().update(game)
                    self.obstacles.remove(obstacle)

                else:
                    self.obstacles.remove(obstacle)


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles =[]

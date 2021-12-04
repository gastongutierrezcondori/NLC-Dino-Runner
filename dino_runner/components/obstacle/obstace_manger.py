import random

import pygame

from components.lives import Lives
from components.obstacle.Cactus import  SmallCactus, LargeCactus, Bird

from components.power_ups.power_ups import hammer
from utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD



class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))



        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    Lives().update(game)
                    self.obstacles.remove(obstacle)
                else:
                    self.obstacles.remove(obstacle)

            elif game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.hammer:
                    Lives().update(game)
                    self.obstacles.remove(obstacle)
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles =[]
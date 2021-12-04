import random

from components.obstacle.Obstacle import Obstacle

class SmallCactus(Obstacle):

    def __init__(self, Image):
        self.type = random.randint(0, 2)
        super().__init__(Image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):

    def __init__(self, Image):
        self.type = random.randint(0, 2)
        super().__init__(Image, self.type)
        self.rect.y = 320

class Bird(Obstacle):

    def __init__(self, Image):
        self.type = 0
        super().__init__(Image, self.type)
        self.rect.y = random.randint(225, 325)
        self.index = 0

    def draw(self, screen):
        if self.index >= 10:
            self.index = 0
        screen.blit(self.image[self.index // 5], self.rect)
        self.index +=1
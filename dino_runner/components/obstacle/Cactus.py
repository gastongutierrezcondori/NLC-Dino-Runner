import random

from components.obstacle.Obstacle import Obstacle

class Cactus(Obstacle):

    def __init__(self, Image):
        self.type = random.randint(0, 2)
        super().__init__(Image, self.type)




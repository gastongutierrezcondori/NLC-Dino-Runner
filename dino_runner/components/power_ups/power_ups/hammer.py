from utils.constants import (
    HAMMER, HAMMER_TYPE
)
from components.power_ups.power_ups.powerup import PowerUp


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super(Hammer, self).__init__(self.image, self.type)
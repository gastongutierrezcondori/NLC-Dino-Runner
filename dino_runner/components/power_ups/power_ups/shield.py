from utils.constants import (
    SHIELD, SHIELD_TYPE
)
from components.power_ups.power_ups.powerup import PowerUp


class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super(Shield, self).__init__(self.image, self.type)

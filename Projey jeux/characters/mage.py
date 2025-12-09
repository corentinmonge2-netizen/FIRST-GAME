from characters.characters import Character
from gears.weapons import old_staff
from gears.armors import mage_robe

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=125, weapon=old_staff, armor=mage_robe)

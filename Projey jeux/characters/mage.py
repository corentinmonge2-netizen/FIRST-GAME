from characters.characters import Character
from gears.weapons import old_staff
from gears.armors import chainmail

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=110, mana=120, weapon=old_staff, armor=chainmail)
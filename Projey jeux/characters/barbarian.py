from characters.characters import Character
from gears.weapons import rusty_sword
from gears.armors import leather

class Barbarian(Character):
    def __init__(self, name):
        super().__init__(name, hp=150, weapon=rusty_sword, armor=leather)

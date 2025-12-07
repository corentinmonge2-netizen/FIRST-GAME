from map.room import Room
from monsters.monsters import get_random_monster, get_boss

class Map:
    def __init__(self, size=5):
        self.rooms = []
        for i in range(size - 1):
            self.rooms.append(Room(get_random_monster()))
        self.rooms.append(Room(get_boss(), is_boss_room=True))

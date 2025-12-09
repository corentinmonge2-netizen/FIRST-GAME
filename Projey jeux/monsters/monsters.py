import random

class Monster:
    def __init__(self, name, hp, dmg, attacks_per_turn=1):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.attacks_per_turn = attacks_per_turn

    def attack(self, target):
        total = 0
        for _ in range(self.attacks_per_turn):
            target.hp -= self.dmg
            total += self.dmg
        print(f"{self.name} attaque {target.name} et inflige {total} dégâts !")


def get_random_monster():
    monsters = [
        Monster("Slime", 100, 10),
        Monster("Dragonnet", 110, 14),
        Monster("Armée de squelettes", 90, 6, attacks_per_turn=2),
        Monster("Loup-garou", 110, 12),
        Monster("Mort-vivant", 89, 12),
        Monster("Této_jockey", 1, 109)
    ]
    return random.choice(monsters)


def get_boss():
    return Monster("Grand Démon", 300, 30, attacks_per_turn=1)

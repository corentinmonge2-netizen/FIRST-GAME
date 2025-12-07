import pickle
import os
from characters.barbarian import Barbarian
from characters.mage import Mage
from map.Map import Map
from gears.weapons import *
from gears.armors import *

LOOT = [
    iron_sword, diamond_sword, iron_axe, diamond_axe,
    magic_staff1, magic_staff2, magic_staff3,
    metal, leather, iron, copper, gold, diamond,
    mage_robe, sage_robe
]


SAVE_FILE = "save.pkl"


def save_game(data):
    with open(SAVE_FILE, "wb") as f:
        pickle.dump(data, f)


def load_game(SAVE_FILE):
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as f:
            return pickle.load(f)
    return None


def choose_class():
    print("Choisissez une classe :")
    print("1 - Barbare")
    print("2 - Magicien")
    c = input("> ")

    name = input("Nom du héros : ")

    if c == "1":
        return Barbarian(name)
    return Mage(name)


def fight(player, monster):
    print(f"\nCombat contre {monster.name} !")

    while monster.hp > 0 and player.hp > 0:
        input("Appuyez sur 'Entré' pour attaquer...")
        player.attack(monster)

        if monster.hp <= 0:
            print("Monstre vaincu !")
            player.hp = player.max_hp
            player.regen_after_fight()
            return True

        monster.attack(player)

        if player.hp <= 0:
            print("Vous êtes mort !")
            return False


def chest_loot(player):
    import random
    loot = random.choice(LOOT)
    print(f"\nVous trouvez un coffre ! Il contient : {loot}")

    choice = input("Voulez-vous l'équiper ? (o/n) : ")

    if choice.lower() == "o":
        if isinstance(loot, Weapon):
            player.equip_weapon(loot)
        else:
            player.equip_armor(loot)


def main():
    save = load_game(SAVE_FILE)
    if save:
        print("Une sauvegarde existe.")
        print("1 - Reprendre")
        print("2 - Nouvelle partie")
        c = input("> ")

        if c == "1":
            player, game_map, current_room = save
        else:
            player = choose_class()
            game_map = Map(6)
            current_room = 0
    else:
        player = choose_class()
        game_map = Map(6)
        current_room = 0

    while current_room < len(game_map.rooms):
        room = game_map.rooms[current_room]
        print(f"\nSalle {current_room+1}/{len(game_map.rooms)}")

        if not fight(player, room.monster):
            print("GAME OVER")
            return

        if not room.is_boss_room:
            chest_loot(player)

        current_room += 1

        save_game((player, game_map, current_room))

    print("\n🎉 Vous avez fini le jeu ! Bravo !")


if __name__ == "__main__":
    main()
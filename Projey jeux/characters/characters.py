class Character:
    def __init__(self, name, hp, mana, weapon, armor):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mana = mana
        self.max_mana = mana
        self.weapon = weapon
        self.armor = armor

    def attack(self, target):
        dmg = self.weapon.damage
        target.hp -= dmg
        print(f"{self.name} attaque {target.name} et inflige {dmg} dégâts !")

    def equip_weapon(self, weapon):
        self.weapon = weapon
        print(f"{self.name} équipe {weapon.name}")

    def equip_armor(self, armor):
        self.armor = armor
        print(f"{self.name} équipe {armor.name}")

    def regen_after_fight(self):
        self.mana = int(self.max_mana * 0.6)
        
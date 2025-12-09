class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.type = type

    def __str__(self):
        return f"{self.name} (DMG +{self.damage})"


iron_sword = Weapon("Épée en fer", 12)
diamond_sword = Weapon("Épée en diamant", 20)

iron_axe = Weapon("Hache en fer", 18)
diamond_axe = Weapon("Hache en diamant", 28)

magic_staff1 = Weapon("Bâton du novice", 10)
magic_staff2 = Weapon("Bâton du sage", 18)
magic_staff3 = Weapon("Bâton archimage", 28)

rusty_sword = Weapon("Épée rouillée", 10)
old_staff = Weapon("Ancien bâton de mage", 9)


fire_ball = Weapon("Boule de feu", 20)
lightning = Weapon("Eclaire", 20)
Frost = Weapon("givre", 20)
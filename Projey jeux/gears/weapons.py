class Weapon:
    def __init__(self, name, damage, type="physical"):
        self.name = name
        self.damage = damage
        self.type = type

    def __str__(self):
        return f"{self.name} (DMG +{self.damage})"


iron_sword = Weapon("Épée en fer", 12)
diamond_sword = Weapon("Épée en diamant", 20)

iron_axe = Weapon("Hache en fer", 18)
diamond_axe = Weapon("Hache en diamant", 28)

magic_staff1 = Weapon("Bâton du novice", 10, type="magical")
magic_staff2 = Weapon("Bâton du sage", 18, type="magical")
magic_staff3 = Weapon("Bâton archimage", 28, type="magical")

rusty_sword = Weapon("Épée rouillée", 8)
old_staff = Weapon("Ancien bâton de mage", 8, type="magical")

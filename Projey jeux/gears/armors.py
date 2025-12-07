class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def __str__(self):
        return f"{self.name} (DEF +{self.defense})"


metal = Armor("Armure en métal", 10)
leather = Armor("Armure de cuir", 7)
iron = Armor("Armure en fer", 12)
copper = Armor("Armure en cuivre", 8)
gold = Armor("Armure en or", 15)
diamond = Armor("Armure en diamant", 25)
chainmail = Armor("Armure en chainmail", 4)

mage_robe = Armor("Robe de mage", 6)
sage_robe = Armor("Robe de grand sage", 14)

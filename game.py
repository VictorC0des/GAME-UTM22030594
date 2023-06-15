class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return self.name


class Player:
    def __init__(self, name, weapons, health):
        self.name = name
        self.weapons = weapons
        self.health = health

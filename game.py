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

    def select_weapon(self):
        # Method for the player to select a weapon
        print(f"{self.name}, select your weapon:")
        for i, weapon in enumerate(self.weapons):
            print(f"{i + 1}. {weapon}")
        choice = int(input("Enter the number of your weapon: ")) - 1
        return self.weapons[choice]

    def attack(self, opponent):
        # Method for the player to attack their opponent
        weapon = self.select_weapon()
        print(f"{self.name} attacks with {weapon.name}!")
        damage = weapon.damage
        print(f"{opponent.name} takes {damage} damage!")
        opponent.lose_health(damage)

    def lose_health(self, damage):
        # Method for the player to lose health
        self.health -= damage
        print(f"{self.name} loses {damage} health. Remaining health: {self.health}")

    def is_defeated(self):
        # Method to check if the player is defeated
        return self.health <= 0

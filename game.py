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

class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        # Method to start the battle
        print(f"{self.player1.name} vs. {self.player2.name}! Let the battle begin!")
        current_turn = 1
        while not self.player1.is_defeated() and not self.player2.is_defeated():
            print(f"\nRound {current_turn}!")
            attacker = self.player1 if current_turn % 2 == 1 else self.player2
            defender = self.player2 if current_turn % 2 == 1 else self.player1
            attacker.attack(defender)
            current_turn += 1
        winner = self.player1 if self.player2.is_defeated() else self.player2
        print(f"\n{winner.name} wins!")


# Create weapons
sword = Weapon("Sword", 30)
axe = Weapon("Axe", 25)
hammer = Weapon("Hammer", 20)
spear = Weapon("Spear", 25)
dagger = Weapon("Dagger", 20)
club = Weapon("Club", 10)

# Get player names from user input
player1_name = input("Enter Player 1 name: ")
player2_name = input("Enter Player 2 name: ")

# Create players with custom names and initial health of 100
player1 = Player(player1_name, [sword, axe, hammer], 100)
player2 = Player(player2_name, [spear, dagger, club], 100)

# Start the battle
battle = Battle(player1, player2)
battle.start()
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0 and self.health > 0:
            return True
        else:
            return False

    def print_status(self):
        print(f'The {self.name} has {self.health} health and {self.power} power.')
class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    def attack(self, enemy):
        self.health -= self.power
        print(f'The goblin does {self.power} damage to you.')
        if hero(self.health) <= 0:
            print("You are dead.")
class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    def attack(self, enemy):
        self.health -= self.power
        print(f'You do {self.power} damage to the goblin.')
        if Goblin(self.health) <= 0:
            print("The goblin is dead.")
    def print_status(self):
        print(f'You have {self.health} health and {self.power} power.')
class Zombie(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    def attack(self, enemy):
        self.health -= self.power
        print(f'The zombie does {self.power} damage to the hero.')
        if Hero(self.health) <= 0:
            print('You\'re dead.')
    def print_status(self):
        print(f'The zombie {self.health} health and {self.power} power.')

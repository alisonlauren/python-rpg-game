print()
print()
print("----------------------------------------------------------------")
print("""Hello Hero! I know you were hoping to take the day
off today, but unfortunately you have encountered a goblin :(""")
print("----------------------------------------------------------------")


class Charachter: 
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))

    def alive(self):
        if self.health > 0 and self.health > 0:
            return True
        else:
            return False

class Hero(Charachter):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def attack(self, enemy):
        # Hero attacks goblin
        enemy.health -= self.power
        print("That'll teach him!!!!!!")
        print("You damaged the goblin by %d levels." % self.power)
        if enemy.health <= 0:
            print("The goblin is dead. Now you can finally take the day off.")

       

class Goblin(Charachter):
    def __init__(self, name):
        super().__init__(name, 30, 10)
    def attack(self, enemy):
        if self.health > 0:
            # Goblin attacks hero
            enemy.health -= self.power
            print("'Ouch, who knew this guy was so strong?")
            print()
            print("The goblin has damaged you by %d levels" %self.power)
            
        if enemy.health <= 0:
            print("Sorry that you're dead now, big bummer.")
        else:
            ("Goblin is still alive")
        
def main():
    goblin = Goblin("Goblin")
    hero = Hero("Hero", 60, 20)

    while goblin.alive() and hero.alive():
        print()
        print()
        print("You're at health level %d, and power level %d." % (hero.health, hero.power))
        print("The Goblin is at health level %d, and power level %d." % (goblin.health, goblin.power))
        print()
        print("What did you want to do? (Choose 1, 2, or 3.)")
        print("1. Are you brave enough to fight the goblin?")
        print("2. Honestly, he doesn't look that scary so, I'm not worried about it.")
        print("3. Fight or flight??! Definitely flight.... I'm out of here.")
        print("------------------------------------------------------------------------- ")
        user_input = input()
        if user_input == "1":
            hero.attack(goblin)
        elif user_input == "2":
            goblin.attack(hero)
        elif user_input == "3":
            goblin.attack(hero)
            print("You can't run away from your problems!!!!")
        else:
            print("Invalid input %r" % user_input)



if __name__ == '__main__':
    main()
   

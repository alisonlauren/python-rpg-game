from charachter import Hero, Goblin, Zombie
def main():
    hero = Hero('Hero', 10, 6)
    goblin = Goblin('Goblin', 6, 1)
    zombie = Zombie('Zombie', 1000, 1)
    while hero.alive() and zombie.alive() or goblin.alive():
        if Goblin.health > 0:
            print('What do you want to do?')
            print('1. Fight goblin')
            print('2. Fight zombie')
            print('3. Do nothing')
            print('4. Flee')
            print('>',)
            user_input = input()
            if user_input == "1":
                Goblin.health -= Hero.power
                print(f'You do {Hero.power} damage to the goblin.')
                if Goblin.health <= 0:
                    Hero.health -= Goblin.power
                    print("The goblin is dead.")
                    Hero.print_status()
                elif Goblin.helth == 0:
                    Hero.health -= Zombie.power
                    print('The zombie just attacked you. It needs to be smited with a holy weapon')
            elif user_input == "2":
                print('The zombie is already dead, you can\'t kill it.')
            elif user_input == '3':
                pass
            elif user_input == "4":
                print("Goodbye.")
                break
            else:
                print(f'Invalid input {user_input}')
            return main()
        else:
            print('What do you want to do?')
            print('1. Fight zombie')
            print('2. Do nothing')
            print('3. Flee')
            print('>',)
            user_input = input()
            if user_input == "1":
                Hero.health -= Zombie.power
                print('The zombie just attacked you. It needs to be smited with a holy weapon')
                Hero.print_status()
            elif user_input == "2":
                pass
            elif user_input == "3":
                print("Goodbye.")
                break
            else:
                print(f'Invalid input {user_input}')
            return main()
main()
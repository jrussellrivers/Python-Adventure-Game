# Changed my mind. Gonna start with the Hero Game. 
# The battle sim was a bit complex and I don't want to just copy Clint's code

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character():
    
    def __init__(self, health=10, power=5):
        self.health = health
        self.power = power

    def is_alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        if self == hero:
            print("\nYou have {0} health and {1} power.".format(hero.health, hero.power))
        if self == goblin:
            print("The goblin has {0} health and {1} power.".format(goblin.health, goblin.power))
    
    def attack(self):
        if self == hero:
            # Hero attacks goblin
            goblin.health -= hero.power
            print("You do {0} damage to the goblin.".format(hero.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
        if self == goblin:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does {0} damage to you.".format(goblin.power))
            if hero.health <= 0:
                print("You are dead.")




class Hero(Character):

    # This is just so it's not empty, weird python thing
    def something(self):
        pass

class Goblin(Character):

    def __init__(self):
        super().__init__()
        self.health = 6
        self.power = 2

def main():

    while goblin.is_alive() and hero.is_alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack()
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {0}".format(user_input))

        if goblin.is_alive():
            goblin.attack()

hero = Hero()
goblin = Goblin()
main()

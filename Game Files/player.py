from items import Gold, Dagger, ShortSword

class Player():
    def __init__(self, name, x, y):
        self.name = name
        self.hp = 100
        self.damage = 5
        self.x = x
        self.y = y
        self.inventory = []

    def check_inventory(self):
        print('')
        for i in self.inventory:
            print(i)
    
    def check_status(self):
        print('''
{0}
=====
HP: {1}
Damage: {2}
'''.format(self.name, self.hp, self.damage))

    def is_alive(self):
        return self.hp > 0
    
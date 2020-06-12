# Gonna make a class for some items

class Item():
    
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return "{0}\n=====\n{1}\nValue: {2}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(
            name = "Gold",
            description = "A round coin with {0} stamped on the front.".format(str(self.amt)),
            value = self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{0}\n=====\n{1}\nValue: {2}\nDamage: {3}".format(self.name, self.description, self.value, self.damage)

class ShortSword(Weapon):
    def __init__(self):
        super().__init__(
            name = 'Short Sword',
            description = 'A sword that is short. Stick \'em with the pointy end',
            value = 20,
            damage = 10
        )

class Dagger(Weapon):
    def __init__(self):
        super().__init__(
            name = "Dagger",
            description = "A small dagger with some rust. Careful where you point it.",
            value = 10,
            damage = 5)

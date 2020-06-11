class Enemy():
    
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def is_alive(self):
        return self.hp > 0

class Bear(Enemy):
    
    def __init__(self):
        super().__init__(name='Bear', hp=35, damage = 13)

class Bandit(Enemy):
    def __init__(self):
        super().__init__(name='Bandit', hp=18, damage = 8)

class Wolf(Enemy):
    def __init__(self):
        super().__init__(name='Wolf', hp=15, damage = 10)
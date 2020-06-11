from enemies import Bear, Bandit, Wolf
from items import Gold, Dagger, ShortSword

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # This is just a template to throw errors
    # Actual maptiles will be a subclass of this
    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

class StartingTile(MapTile):
    def intro_text(self):
        return """
        put starting tile intro here
        """

    def modify_player(self, player):
        # Tile has no action on player
        pass

# ---------------------------------------------------------

class LootTile(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class FindDaggerTile(LootTile):
    def __init__(self, x, y):
        super().__init__(x, y, Dagger())

    def intro_text(self):
        return """
        You notice something shiny behind a rock.
        It's a dagger! You pick it up.
        """

class FindGoldTile(LootTile):
    def __init__(self, x, y):
        super().__init__(x, y, Gold())

    def intro_text(self):
        return """
        You find some gold pieces scattered about the forest floor.
        """
# ---------------------------------------------------------

class EnemyTile(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x,y)
    
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {0} damage. You have {1} HP remaining.".format(self.enemy.damage, player.hp))

class BanditTile(EnemyTile):
    def __init__(self, x, y):
        super().__init__(x, y, Bandit())

    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            You've been ambushed by a bandit!
            '''
        else:
            return '''
            A bandit lays dead on the ground.
            '''

class BearTile(EnemyTile):
    def __init__(self, x, y):
        super().__init__(x, y, Bear())

    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            A wild bear has appeared!
            '''
        else:
            return '''
            A dead bear lays sprawled out on the forest floor.
            '''

class WolfTile(EnemyTile):
    def __init__(self, x, y):
        super().__init__(x, y, Wolf())

    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            A wild wolf has appeared!
            '''
        else:
            return '''
            A dead wolf lays sprawled out on the forest floor.
            '''




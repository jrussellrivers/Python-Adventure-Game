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
    def __init__(self, x, y):
        self.start_num = 0
        super().__init__(x,y)

    def intro_text(self):
        if self.start_num == 0:
            self.start_num += 1
            return """
        Welcome to the oddly dangerous patch of forest.
        Moderately valuable treasures await you inside!
            """
        else:
            return '''
        Welcome back to the start. Time to go another direction!
            '''

    def modify_player(self, player):
        # Tile has no action on player
        pass

    def start_forest(self):
        start_ran = True
        while start_ran:
            start_input = input('Would you like to enter the forest? (Y/N) ')
            if start_input != 'Y' and start_input != 'N':
                print('Invalid Input')
            elif start_input == 'N':
                print('Goodbye')
                exit()
            else:
                start_ran = False

class EmptyForestTile(MapTile):
    def intro_text(self):
        return '''
        This part of the forest seems remarkably pointless.
        '''
    
    def modify_player(self, player):
        pass

class LeaveForestTile(MapTile):
    def intro_text(self):
        return '''
        You've made it to the forest exit!
        Time to leave. Wasn't that thrilling?
        '''
    
    def modify_player(self, player):
        pass

    def leave(self):
        leaving = True
        while leaving:
            leave_input = input('Would you like to leave the forest? (Y/N) ')
            if leave_input != 'Y' and leave_input != 'N':
                print('Invalid Input')
            elif leave_input == 'Y':
                print('\nGoodbye')
                exit()
            else:
                leaving = False

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
    
    def return_text(self):
        return """
        There's an imprint in the grass where a dagger used to be.
        Nothing else is of interest here.
        """

class FindGoldTile(LootTile):
    def __init__(self, x, y):
        super().__init__(x, y, Gold(5))

    def intro_text(self):
        return """
        You find some gold pieces scattered about the forest floor.
        """
    
    def return_text(self):
        return """
        Sadly no one else has left their precious currency here.
        Go find gold in some other forest.
        """

class FindShortSwordTile(LootTile):
    def __init__(self, x, y):
        super().__init__(x, y, ShortSword())
    
    def intro_text(self):
        return """
        You notice something leaned up against a tree.
        It's a shortsword! You pick it up.
        """
    def return_text(self):
        return """
        There is no more carlelessly placed weaponry to find.
        Carry on now.
        """
# ---------------------------------------------------------

class EnemyTile(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x,y)
    
    def modify_player(self, player):
        
        while self.enemy.is_alive() and player.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {0} damage. You have {1} HP remaining.".format(self.enemy.damage, player.hp))
            for item in player.inventory:
                if type(item) == Gold:
                    pass
                elif item.damage > player.damage:
                    player.damage = item.damage
            self.enemy.hp = self.enemy.hp - player.damage
            if self.enemy.is_alive():
                print("Player does {0} damage. Enemy has {1} HP remaining.\n".format(player.damage, self.enemy.hp))
            else:
                print("Player does {0} damage. Enemy has been slain.\n".format(player.damage))
        if not player.is_alive():
            print('You have died')
            print('Goodbye')
            exit()

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

start = StartingTile(0,0)
dagger_tile = FindDaggerTile(0,-1)
wolf_tile = WolfTile(-2,0)
empty1 = EmptyForestTile(-1,0)
empty2 = EmptyForestTile(0,1)
gold_tile = FindGoldTile(0,2)
empty3 = EmptyForestTile(1,2)
sword_tile = FindShortSwordTile(-1,2)
bear_tile = BearTile(-1,3)
bandit_tile = BanditTile(1,3)
leave_tile1 = LeaveForestTile(-1,4)
leave_tile2 = LeaveForestTile(1,4)


proper_tiles = [
    (0,0), 
    (0,-1),
    (-1,0),
    (-2,0),
    (0,1),
    (0,2),
    (1,2),
    (1,3),
    (1,4),
    (-1,2),
    (-1,3),
    (-1,4)
    ]
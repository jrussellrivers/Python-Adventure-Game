# from tiles import start, dagger_tile, wolf_tile
from items import Gold, Dagger, ShortSword

class Player():
    def __init__(self, name, x, y):
        self.name = name
        self.hp = 100
        self.damage = 15
        self.x = x
        self.y = y
        self.inventory = [Gold(5), Dagger()]

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
    
# # Everything below this is a test



# player1 = Player('Jordan', 0, 0)

# if player1.x == start.x and player1.y == start.y:
#     print(start.intro_text())
#     start.start_forest()

# print('''
# Which direction would you like to go?

# 1. North
# 2. East
# 3. South
# 4. West
# ''')
# dir_input = input('')

# if dir_input == '3':
#     player1.y -= 1
# elif dir_input == '2':
#     player1.x += 1

# if player1.x == dagger_tile.x and player1.y == dagger_tile.y:
#     print(dagger_tile.intro_text())
#     dagger_tile.modify_player(player1)
    
# print('''
# Which direction would you like to go?

# 1. North
# 2. East
# 3. South
# 4. West
# ''')
# dir_input = input('')

# if dir_input == '1':
#     player1.y += 1

# if player1.x == start.x and player1.y == start.y:
#     print(start.intro_text())



# if player1.x == wolf_tile.x and player1.y == wolf_tile.y:
#     print(wolf_tile.intro_text())
#     wolf_tile.modify_player(player1)

# # FOR IF THE USER WANTS TO LOOK AT INVENTORY

# # for i in player1.inventory:
# #     # print(type(i))
# #     # if type(i) == Dagger:
# #     #     print('Im a dagger')
# #     # elif type(i) == Gold:
# #     #     print(i.value)
# #     print(i)
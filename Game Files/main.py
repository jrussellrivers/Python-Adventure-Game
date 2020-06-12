from player import Player
from items import Gold, Dagger, ShortSword
from tiles import start, dagger_tile, wolf_tile, empty1, empty2, empty3, gold_tile, sword_tile, bandit_tile, bear_tile, leave_tile1, leave_tile2

name_input = input('\nPlease enter your name: ')
player1 = Player(name_input, 0, 0)

print(start.intro_text())
start.start_forest()

game = True
while game:
    print('''
What would you like to do?

1. Go North
2. Go East
3. Go South
4. Go West
5. Check Inventory
6. Check Player Status
''')
    player_input = input('')
    if player_input == '1':
        player1.y += 1
    elif player_input == '2':
        player1.x += 1
    elif player_input == '3':
        player1.y -= 1
    elif player_input == '4':
        player1.x -= 1
    elif player_input == '5':
        player1.check_inventory()
    elif player_input == '6':
        player1.check_status()
    else:
        print('Invalid Input')
    
    print(player1.x)
    print(player1.y)
    
    
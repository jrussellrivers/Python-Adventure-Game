from player import Player
from items import Gold, Dagger, ShortSword
from tiles import start, dagger_tile, wolf_tile, empty1, empty2, empty3, gold_tile, sword_tile, bandit_tile, bear_tile, leave_tile1, leave_tile2, proper_tiles

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
        location = (player1.x, player1.y)
        if location not in proper_tiles:
            print('\nThe forest in that direction is too difficult to traverse.\nYou must find another path.')
            player1.y -= 1
    elif player_input == '2':
        player1.x += 1
        location = (player1.x, player1.y)
        if location not in proper_tiles:
            print('\nThe forest in that direction is too difficult to traverse.\nYou must find another path.')
            player1.x -= 1
    elif player_input == '3':
        player1.y -= 1
        location = (player1.x, player1.y)
        if location not in proper_tiles:
            print('\nThe forest in that direction is too difficult to traverse.\nYou must find another path.')
            player1.y += 1
    elif player_input == '4':
        player1.x -= 1
        location = (player1.x, player1.y)
        if location not in proper_tiles:
            print('\nThe forest in that direction is too difficult to traverse.\nYou must find another path.')
            player1.x += 1
    elif player_input == '5':
        player1.check_inventory()
    elif player_input == '6':
        player1.check_status()
    else:
        print('Invalid Input')
    
    print('X: ' + str(player1.x))
    print('Y: ' + str(player1.y))

    tile = True
    while tile:
        if player1.x == start.x and player1.y == start.y:
            print(start.intro_text())
        tile = False
    
    tile = True
    while tile:
        if player1.x == dagger_tile.x and player1.y == dagger_tile.y:
            found = False
            for item in player1.inventory:
                if type(item) == Dagger:
                    found = True
            if not found:
                print(dagger_tile.intro_text())
                dagger_tile.modify_player(player1)
            else:
                print(dagger_tile.return_text())
                
        tile = False

    tile = True
    while tile:
        if player1.x == wolf_tile.x and player1.y == wolf_tile.y:
            print(wolf_tile.intro_text())
            wolf_tile.modify_player(player1)
        tile = False

    print(player1.inventory)
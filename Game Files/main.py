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
            print('''
        The forest in that direction is too dsifficult to traverse.
        You must find another path.
            ''')
            player1.y -= 1
    elif player_input == '2':
        player1.x += 1
        location = (player1.x, player1.y)
        if location not in proper_tiles:
            print('''
        The forest in that direction is too dsifficult to traverse.
        You must find another path.
            ''')
            player1.x -= 1
    elif player_input == '3':
        player1.y -= 1
        location = (player1.x, player1.y)
        if location not in proper_tiles:
            print('''
        The forest in that direction is too dsifficult to traverse.
        You must find another path.
            ''')
            player1.y += 1
    elif player_input == '4':
        player1.x -= 1
        location = (player1.x, player1.y)
        if location not in proper_tiles:
            print('''
        The forest in that direction is too difficult to traverse.
        You must find another path.
            ''')
            player1.x += 1
    elif player_input == '5':
        player1.check_inventory()
    elif player_input == '6':
        for item in player1.inventory:
                if type(item) == Gold:
                    pass
                elif item.damage > player1.damage:
                    player1.damage = item.damage
        player1.check_status()
    else:
        print('Invalid Input')

    tile = True
    while tile:
        if player1.x == start.x and player1.y == start.y:
            print(start.intro_text())
            tile = False
        elif player1.x == dagger_tile.x and player1.y == dagger_tile.y:
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
        elif player1.x == wolf_tile.x and player1.y == wolf_tile.y:
            print(wolf_tile.intro_text())
            wolf_tile.modify_player(player1)
            tile = False
        elif player1.x == gold_tile.x and player1.y == gold_tile.y:
            found = False
            for item in player1.inventory:
                if type(item) == Gold:
                    found = True
            if not found:
                print(gold_tile.intro_text())
                gold_tile.modify_player(player1)
            else:
                print(gold_tile.return_text())
            tile = False
        elif player1.x == sword_tile.x and player1.y == sword_tile.y:
            found = False
            for item in player1.inventory:
                if type(item) == ShortSword:
                    found = True
            if not found:
                print(sword_tile.intro_text())
                sword_tile.modify_player(player1)
            else:
                print(sword_tile.return_text())
            tile = False
        elif player1.x == bear_tile.x and player1.y == bear_tile.y:
            print(bear_tile.intro_text())
            bear_tile.modify_player(player1)
            tile = False
        elif player1.x == bandit_tile.x and player1.y == bandit_tile.y:
            print(bandit_tile.intro_text())
            bandit_tile.modify_player(player1)
            tile = False
        elif player1.x == empty1.x and player1.y == empty1.y:
            print(empty1.intro_text())
            tile = False
        elif player1.x == empty2.x and player1.y == empty2.y:
            print(empty2.intro_text())
            tile = False
        elif player1.x == empty3.x and player1.y == empty3.y:
            print(empty3.intro_text())
            tile = False
        elif player1.x == leave_tile1.x and player1.y == leave_tile1.y:
            print(leave_tile1.intro_text())
            leave_tile1.leave()
        elif player1.x == leave_tile2.x and player1.y == leave_tile2.y:
            print(leave_tile2.intro_text())
            leave_tile2.leave()
        else:
            pass
        tile = False

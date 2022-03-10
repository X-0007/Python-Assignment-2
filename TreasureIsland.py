''' MODULE FOR THE TREASURE HUNTING ISLAND PROGRAM '''


def treasureIsland():
    print('Welcome to Treasure Island.\nYour mission is to find the treasure.')
    direction = input('left or right\n')
    if direction == 'Left':
        action = input('\nswim or wait\n')
        if action == 'Wait':
            door = input('\nWhich door?\n')
            if door == 'Red':
                print('Burned by fire.\nGame Over.')
            if door == 'Blue':
                print('Eaten by beasts.\nGame Over.')
            elif door == 'Yellow':
                print('You Win!')
            else:
                print('Game Over.')
        else:
            print('Attacked by Trout.\nGame Over.')
    else:
        print('Fall into a hole.\nGame Over.')



game = [int(input("How many stones the first stack has?")),int(input("How many stones the second stack has?"))]
if (game[0] % 2) != 0 and (game[1] % 2) != 0:
    print("Remove one from both")
    game[0] = game[0]-1
    game[1] = game[1]-1
    print(game, "This is a winning situation")
if (game[0] % 2) == 0 and (game[1] % 2) == 0:
    print("This is a lose situation")
if (game[0] % 2) == 0 and (game[1] % 2) != 0:
    print("Remove one from the right pabble")
    game[1] = game[1]-1
    print(game, "This is a winning situation")
if (game[0] % 2) != 0 and (game[1] % 2) == 0:
    print("Remove one from the left pabble")
    game[0] = game[0]-1
    print(game, "This is a winning situation")

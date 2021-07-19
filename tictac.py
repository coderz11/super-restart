game = [[0, 0, 0],
        [0, 0, 0], 
        [0, 0, 0]]

def game_board(game_map, player=0, row=0, column=0, justDisplay=False):
    try:
        print("   0  1  2")
        if not justDisplay:
            game_map[row][column] = player 
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print("Error : Did you input row column as 0 1 or 2?", e)
    except Exception as e:
        print("Something went very wrong!", e)

game_board(game, justDisplay=True)
game_board(game_board, player=1, row=3, column=1)
#game[0][1] = 1
#game_board()
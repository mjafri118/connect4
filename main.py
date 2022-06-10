import numpy as np

zero = np.array([
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,]
 ])

gameNoWinner = np.array([
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,],
 [0, 0, 0, 0, 0, 0, 0,],
 [2, 0, 0, 2, 0, 0, 0,]
 ])
print(gameNoWinner)

def generateNextPlay(og_game, turnID, move):
    nextPlay = og_game
    for i in range(len(nextPlay)):
        if np.flip(nextPlay,axis=0)[i][move] == 0:
            print(f'OLD PLAY:')
            print(og_game)

            np.flip(nextPlay,axis=0)[i][move] = turnID

            print(f"NEXT PLAY with move {move}")
            print(nextPlay)
            return nextPlay
    return nextPlay


def filterLosingMoves(game, turnID, moves):
    # TODO
    return moves
    # for move in moves:
    #     nextPlay = generateNextPlay(game, turnID, move)

def getWinningMove(game, turnID, moves):
    og_game = game
    for move in moves: 
        nextPlay = generateNextPlay(og_game, turnID, move)
        if compute_winner(nextPlay) == turnID: return {'exists': True, 'move': move}
    return {'exists': False, 'move': -1}

def filterIllegalMoves(game, turnID, moves):
    legalMoves = []
    for move in moves:
        if (game[0][move] != 0):
            # print(f"This column is illegal: {move}")
            continue
        legalMoves.append(move)
    return legalMoves

# given a 1D array of any length, returns the ID of any 4-in-a-row-winner, else 0.
def get_line_winner(array):
    # no small array can have 4 in a row.
    if len(array) < 4:
        return 0

    # return array.count(array[0]) == len(array) and (horizontal[i] != 0)
    LIMIT = len(array) - 3
    for i in range(len(array)):
        if i == LIMIT:
            break
        slide = [array[i], array[i+1], array[i+2], array[i+3]]
        if (slide.count(slide[0]) == len(slide) and (array[i] != 0)):
            # print(f"WINNER: {array[i]}")
            return array[i]

def compute_winner(game):
    # horizontals: check each horizontals
    for horizontal in game: 
        winner = get_line_winner(horizontal)
        if winner: return winner
            
    # verticals
    for vertical in np.transpose(game): 
        winner = get_line_winner(vertical)
        if winner: return winner

    # diagonals
    for i in range(2):
        game_to_use = np.flip(game, axis=(1)) if i else game

        # horizontals
        for i in range(0,7):
            # print(f'starting at {game_to_use[0][i]}')
            array = []
            try:
                for j in range(7):
                    array.append(game_to_use[0+j][i+j])
            except:
                winner = get_line_winner(array)
                if winner: return winner
        # verticals
        for i in range(0,6):
            # print(f'starting at {game_to_use[i][0]}')
            array = []
            try:
                for j in range(7):
                    array.append(game_to_use[i+j][0+j])
            except:
                winner = get_line_winner(array)
                if winner: return winner

    # print('NO WINNER')
    return 0

def compute_next_move(game, turnID):
    # base case: if there is already a winner
    winner = compute_winner(game)
    if (winner): return {False, -1} 

    moves = np.arange(0,len(game[0]))

    moves = filterIllegalMoves(game, turnID, moves)

    winningMove = getWinningMove(game, turnID, moves) 
    if (winningMove['exists']): return {True, str(winningMove['move'])}

    # moves = filterLosingMoves(game, turnID, moves) 
    # moves = rankBestMove(game, turnID)
    print(moves)

print(compute_next_move(gameNoWinner, 2))

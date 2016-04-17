"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 50         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
def mc_trial(board, player):
    """
     Takes a current board and the next player to move. 
     The function should play a game starting with the given player by making random moves, 
     alternating between players. The function should return when the game is over. 
     The modified board will contain the state of the game, so the function does not return anything. 
    """
    while not board.check_win():
        next_square = random.choice(board.get_empty_squares())
        board.move(next_square[0], next_square[1], player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    """
    Takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, 
    a board from a completed game, and which player the machine player is. 
    The function should score the completed board and update the scores grid. 
    As the function updates the scores grid directly, it does not return anything,
    """
    if board.check_win() is provided.DRAW:
        return

    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            if board.check_win() is player and board.square(row, col) is player:
                scores[row][col] += 1
            elif board.check_win() is player and board.square(row, col) is not 1: 
                scores[row][col] -= 1
            elif board.check_win() not in [1, player] and board.square(row, col) is player:
                scores[row][col] -= 1
            elif board.check_win() not in [1, player] and board.square(row, col) not in [1, player]: 
                scores[row][col] += 1

def get_best_move(board, scores):
    """
    Takes a current board and a grid of scores. The function should find all of 
    the empty squares with the maximum score and randomly return one of them as a tuple. 
    It is an error to call this function with a board that has no empty squares (there is no possible next move) 
    so your function may do whatever it wants in that case. The case where the board is full will not be tested.
    """
    max_score = None
    best_move = None
    empty_squares = board.get_empty_squares()
    
    if len(empty_squares) == 1:
        return empty_squares[0]

    for square in empty_squares:
        square_score = scores[square[0]][square[1]]
        if square_score > max_score or max_score is None:
            max_score = square_score
            best_move = square

    return best_move

def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine player is, and the number of trials to run. 
    The function should use the Monte Carlo simulation described above to return a move for the
    machine player in the form of a tuple. Be sure to use the other functions you have written!
    """
    scores = [[0 for _ in range(board.get_dim())] for _ in range(board.get_dim())]
    
    for _ in range(trials):
        board_clone = board.clone()
        mc_trial(board_clone, player)
        mc_update_scores(scores, board_clone, player)
    
    return get_best_move(board, scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

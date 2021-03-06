"""
Mini-max Tic-Tac-Toe Player
"""

#import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
# import codeskulptor
# codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """

    if board.check_win() is not None:
        return SCORES[board.check_win()], (-1, -1)
    
    empty_squares = board.get_empty_squares()
    sign = 1 if player is provided.PLAYERX else -1
    
    score = -2
    move = (-1, -1)

    for square in empty_squares:
        next_board = board.clone()
        next_player = provided.switch_player(player)
        row, col = square[0], square[1]
        next_board.move(row, col, player)
        temp_score, _ = mm_move(next_board, next_player)
        
        if temp_score * sign == 1 or temp_score * sign > score:
            score = temp_score
            move = (row, col)

    return score, move

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

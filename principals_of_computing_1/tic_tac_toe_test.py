import pytest, unittest
from mock import Mock
from tic_tac_toe import mc_trial, mc_update_scores, get_best_move, mc_move
import poc_ttt_provided as provided

class TestMC(object):

	@pytest.fixture(autouse=True)
	def setup(self):
		self.dim = 3
		self.test_board = provided.TTTBoard(self.dim)
		self.test_scores = [[0 for x in range(self.dim)] for x in range(self.dim)]
		self.test_playerx_loosing_board = provided.TTTBoard(self.dim, board = [[3, 2, 2], [3, 1, 2], [3, 2, 3]])
		self.test_playerx_winning_board = provided.TTTBoard(self.dim, board = [[2, 3, 3], [2, 1, 3], [2, 3, 2]])
		
		self.test_board_one_square_empty = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
        	[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]])
		
		self.test_board_two_best_squares = provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], 
			[provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.EMPTY, provided.EMPTY]])
		
		self.mc_move_board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY], 
			[provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]])
		
		self.trials = 50

	def test_mc_trial(self):
		# when
		trial = mc_trial(self.test_board, provided.PLAYERX)

		# then
		assert trial is None
		assert self.test_board.check_win() is not None

	def test_mc_update_scores_playerx_loosing(self):
		
		# when
		playerx_loosing_scores = mc_update_scores(self.test_scores, self.test_playerx_loosing_board, provided.PLAYERX)
		
		# then
		assert playerx_loosing_scores is None
		assert self.test_scores == [[1, -1, -1], [1, 0, -1], [1, -1, 1]]

	def test_mc_update_scores_playerx_winning(self):
		
		# when
		playerx_winning_scores = mc_update_scores(self.test_scores, self.test_playerx_winning_board, provided.PLAYERX)
		
		# then
		assert playerx_winning_scores is None
		assert self.test_scores == [[1, -1, -1], [1, 0, -1], [1, -1, 1]]
	
	def test_get_best_move_one_square_empty(self):

		#when
		move = get_best_move(self.test_board_one_square_empty,  [[3, 2, 5], [8, 2, 8], [4, 0, 2]])

		# then
		assert move == (2, 1)

	def test_get_best_move_two_best_squares(self):

		#when
		best_move = get_best_move(self.test_board_two_best_squares,  [[-3, 6, -2], [8, 0, -3], [3, -2, -4]])

		# then
		assert best_move == (0, 2)

	def test_mc_move_returns_best_move(self):

		# when
		best_move = mc_move(self.mc_move_board, provided.PLAYERX, self.trials)

		#then
		assert best_move == (1, 2)



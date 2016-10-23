import pytest, unittest
from mock import Mock
from ttt_minimax import mm_move
import poc_ttt_provided as provided


class TestTTTMinimax(object):

	@pytest.fixture(autouse=True)
	def setup(self):
		self.dim = 3
		self.test_playerx_winning_board = provided.TTTBoard(self.dim, False, [[provided.PLAYERX, provided.PLAYERO, provided.PLAYERO], 
			[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])
		self.test_playero_winning_board = provided.TTTBoard(self.dim, False, [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], 
			[provided.PLAYERO, provided.PLAYERO, provided.PLAYERX], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERO]])
		self.test_draw_board = provided.TTTBoard(self.dim, False, [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERO], 
			[provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERX, provided.PLAYERO, provided.PLAYERO]])

	def test_playerx_wins(self):
		# when
		result = mm_move(self.test_playerx_winning_board, provided.PLAYERO)

		# then
		assert result ==  (1, (-1, -1))


	def test_playero_wins(self):
		# when
		result = mm_move(self.test_playero_winning_board, provided.PLAYERX)

		# then
		assert result ==  (-1, (-1, -1))

	def test_draw(self):
		# when
		result = mm_move(self.test_draw_board, provided.PLAYERO)

		# then
		assert result ==  (0, (-1, -1))


	def test_one_move_playerx_wins(self):
		# given
		board = provided.TTTBoard(self.dim, False, [[provided.PLAYERO, provided.PLAYERX, provided.EMPTY], 
			[provided.PLAYERO, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])
		
		# when
		result = mm_move(board, provided.PLAYERX)

		# then
		assert result == (1, (0, 2))

	def test_one_move_playerx_draw(self):
		# given
		board = provided.TTTBoard(self.dim, False, [[provided.PLAYERO, provided.PLAYERX, provided.PLAYERO], 
			[provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.PLAYERX, provided.PLAYERO, provided.PLAYERX]])
		
		# when
		result = mm_move(board, provided.PLAYERX)

		# then
		assert result == (0, (1, 2))

	def test_something(self):
		# given
		board = provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], 
			[provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]])
		
		# when
		result = mm_move(board, provided.PLAYERO)

		# then
		assert result == (-1, (2, 1))
	
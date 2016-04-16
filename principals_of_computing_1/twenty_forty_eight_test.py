
import pytest, unittest
from twenty_forty_eight import TwentyFortyEight

# Direction constants
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

class TestTwentyFortyEight(object):
	@pytest.fixture(autouse=True)
	def setup(self):
		self.game = TwentyFortyEight(2, 3)
		self.test_empty_grid = [[0,0,0,0], [0,0,0,0], [0,0,0,0], 
								[0,0,0,0], [0,0,0,0], [0,0,0,0]]

		self.test_non_empty_grid = [[0,2,0,0], [0,4,0,0], [32,8,4,0], 
									[0,4,0,4], [0,2,0,8], [2,2,16,0]]

	def test_init_creates_grid_with_two_tiles(self):

		# then
		assert self.game._grid is not self.test_empty_grid
		assert len(self.game._grid) == 2
	
	def test_get_grid_height_returns_height(self):
		# when
		height = self.game.get_grid_height()

		# then
		assert height == 2

	def test_get_grid_width_returns_width(self):
		# when
		width = self.game.get_grid_width()
		
		# then
		assert width == 3
	
	def test_set_new_tile_sets_correctly(self):
		
		# when
		self.game.set_tile(1, 1, 6)

		# then 
		assert self.game._grid[1][1] == 6

	def test_get_new_tile_sets_correctly(self):
		# given
		self.game.set_tile(1, 1, 6)

		# when
		val = self.game.get_tile(1, 1)

		# then 
		assert val == 6

	def test_merge_up_success(self):
		# given
		self.game._grid = [[2,2,0], 
						  [2,4,4]]

		expected_result = [[4,2,4], 
						   [0,4,0]] 
						   
		# when
		self.game.move(UP)

		# then
		assert self.game._grid == expected_result

	def test_merge_down_success(self):
		# given
		self.game._grid = [[2,2,8], 
						  [2,0,8]]

		expected_result = [[0,0,0], 
						   [4,2,16]] 
						   
		# when
		self.game.move(DOWN)

		# then

		assert self.game._grid == expected_result

	def test_merge_left_success(self):
		# given
		self.game._grid = [[2,2,0], 
						  [2,4,4]]

		expected_result = [[4,0,0], 
						   [2,8,0]] 
						   
		# when
		self.game.move(LEFT)

		# then

		assert self.game._grid == expected_result

	def test_merge_right_success(self):
		# given
		self.game._grid = [[2,2,0], 
						  [2,4,4]]

		expected_result = [[0,0,4], 
						   [0,2,8]] 
						   
		# when
		self.game.move(RIGHT)

		# then
		
		assert self.game._grid == expected_result









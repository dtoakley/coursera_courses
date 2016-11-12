import pytest, unittest
from mock import Mock
from fifteen import Puzzle

class TestPuzzle(object):

	@pytest.fixture(autouse=True)
	def setup(self):
		self.test_lower_right_true_1 = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 10], [9, 1, 14, 11], [12, 13, 0, 15]])
		self.test_lower_right_true_2 = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 10], [9, 1, 0, 11], [12, 13, 14, 15]])
		self.test_lower_right_true_3 = Puzzle(4, 4, [[4, 2, 3, 1], [5, 0, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
		self.test_lower_right_true_4 = Puzzle(4, 4, [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]])
		self.test_lower_right_false_1 = Puzzle(4, 4, [[4, 2, 15, 7], [8, 5, 6, 10], [12, 1, 0, 11], [9, 13, 14, 3]])
		self.test_lower_right_false_2 = Puzzle(4, 4, [[4, 2, 3, 7], [8, 5, 6, 10], [12, 15, 0, 11], [9, 13, 14, 1]])
		self.test_lower_right_false_3 = Puzzle(4, 4, [[4, 2, 3, 1], [5, 0, 6, 7], [8, 9, 10, 11], [13, 12, 14, 15]])
		self.test_lower_right_false_4 = Puzzle(4, 4, [[0, 1, 2, 3], [7, 4, 6, 5], [8, 9, 10, 11], [12, 13, 14, 15]])

	def test_lower_row_invariant_true_1(self):
		# when
		result = self.test_lower_right_true_1.lower_row_invariant(3, 2)

		# then
		assert result == True
		
	def test_lower_row_invariant_true_2(self):
		# when
		result = self.test_lower_right_true_2.lower_row_invariant(2, 2)

		# then

	def test_lower_row_invariant_true_3(self):
		# when
		result = self.test_lower_right_true_3.lower_row_invariant(1, 1)

		# then
		assert result == True

	def test_lower_row_invariant_true_4(self):
		# when
		result = self.test_lower_right_true_4.lower_row_invariant(0, 0)

		# then
		assert result == True

	def test_lower_row_invariant_true_5(self):
		# given 
		test_puzzle = Puzzle(4, 5, [[7, 12, 11, 5, 3], [6, 2, 10, 9, 4], [1, 8, 13, 14, 0], [15, 16, 17, 18, 19]])

		# when
		result = test_puzzle.lower_row_invariant(2, 4)

		# then
		assert result == True

	def test_lower_row_invariant_false_1(self):
		# when
		result = self.test_lower_right_false_1.lower_row_invariant(3, 2)

		# then
		assert result == False

	def test_lower_row_invariant_false_2(self):
		# when
		result = self.test_lower_right_false_2.lower_row_invariant(2, 2)

		# then
		assert result == False

	def test_lower_row_invariant_false_3(self):
		# when
		result = self.test_lower_right_false_3.lower_row_invariant(1, 1)

		# then
		assert result == False

	def test_lower_row_invariant_false_4(self):
		# when
		result = self.test_lower_right_false_4.lower_row_invariant(0, 0)

		# then
		assert result == False

	def test_lower_row_invarient_false_5(self):
		# given
		test_puzzle = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])

		# when
		result = test_puzzle.lower_row_invariant(2, 0)

		# then
		assert result == False

	def test_lower_row_invarient_false_6(self):
		# given
		test_puzzle = Puzzle(4, 5, [[15, 11, 10, 9, 8], [7, 6, 5, 4, 3], [2, 1, 0, 13, 14], [12, 16, 17, 18, 19]])

		# when
		result = test_puzzle.lower_row_invariant(2, 2)

		# then
		assert result == False

	def test_solve_interior_tile_1(self):
		# given
		test_puzzle = Puzzle(4, 4, [[6, 2, 3, 7], [8, 5, 14, 10], [9, 1, 11, 12], [13, 4, 0, 15]])

		# when
		assert test_puzzle.lower_row_invariant(3, 2)
		result = test_puzzle.solve_interior_tile(3, 2)
		print test_puzzle
		assert test_puzzle.lower_row_invariant(3, 1)

		# then
		assert result == "uulddruld"

	def test_solve_interior_tile_2(self):
		# given
		test_puzzle = Puzzle(4, 4, [[11, 2, 3, 7], [8, 5, 6, 10], [9, 1, 11, 14], [13, 4, 0, 15]])

		# when
		assert test_puzzle.lower_row_invariant(3, 2)
		result = test_puzzle.solve_interior_tile(3, 2)
		assert test_puzzle.lower_row_invariant(3, 1)

		# then
		assert result == "urullddruld"

	def test_solve_interior_tile_2(self):
		# given
		test_puzzle = Puzzle(3, 3, [[8, 7, 6], [5, 4, 3], [2, 1, 0]])

		# when
		assert test_puzzle.lower_row_invariant(2, 2)
		result = test_puzzle.solve_interior_tile(2, 2)
		assert test_puzzle.lower_row_invariant(2, 1)

		# then
		assert result == "uulldrruldrulddruld"

	def test_solve_col0_1(self):
		# given
		test_puzzle = Puzzle(3, 3, [[3, 2, 1], [6, 5, 4], [0, 7, 8]])

		# when
		assert test_puzzle.lower_row_invariant(2, 0)
		result = test_puzzle.solve_col0_tile(2)
		assert test_puzzle.lower_row_invariant(1, 2)

		# then
		assert result == "urr"

	def test_solve_col0_2(self):
		# given
		test_puzzle = Puzzle(4, 5, [[12, 11, 10, 9, 15], [7, 6, 5, 4, 3], [2, 1, 8, 13, 14], [0, 16, 17, 18, 19]])

		# when
		assert test_puzzle.lower_row_invariant(3, 0)
		result = test_puzzle.solve_col0_tile(3)
		print test_puzzle
		assert test_puzzle.lower_row_invariant(2, 4)

		# then
		assert result == "uruurrrdllurdllurdlludrulddruldruldrdlurdluurddlurrrr"

	def test_row0_invarien_1(self):
		# given 
		test_puzzle = Puzzle(3, 3, [[0, 1, 2], [3, 4, 5], [6, 7, 8]])

		# when
		result = test_puzzle.row0_invariant(0)

		# then
		assert result == True

	def test_row0_invarient_2(self):
		# given 
		test_puzzle = Puzzle(4, 5, [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])

		# when
		result = test_puzzle.row0_invariant(0)

		# then
		assert result == True

	def test_solve_row0_1(self):
		# given
		test_puzzle = Puzzle(3, 3, [[4, 1, 0], [2, 3, 5], [6, 7, 8]])

		# when
		result = test_puzzle.solve_row0_tile(2)

		# then
		assert result == ""



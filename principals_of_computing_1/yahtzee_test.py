import pytest, unittest
from yahtzee import gen_all_sequences, score, expected_value, gen_all_holds, strategy

class TestYahtzee(object):
	@pytest.fixture(autouse=True)

	def test_score(self):
		# given
		hand1 = (1,2,3,3,5)
		hand2 = (2,2,2,2,5)
		hand3 = (2,2,2,5,5)
		
		# when
		result1 = score(hand1)
		result2 = score(hand2)
		result3 = score(hand3)

		# then
		assert result1 == 6
		assert result2 == 8
		assert result3 == 10

	def test_expected_value(self):
		# given
		hand1 = (4,4,4,4)
		hand2 = (2,2,2,2)
		hand3 = (2,2)

		# when
		result1 = expected_value(hand1, 6, 1)
		result2 = expected_value(hand2, 6, 1)
		result3 = expected_value(hand3, 6, 2)

		# then
		assert abs(result1 - 16.6) < 0.1
		assert abs(result2 -8.3) < 0.1
		assert abs(result3 - 5.83) < 0.1

	def test_gen_all_holds(self):

		#given 
		hand = (1,2,3,4,5)

		# when
		result = gen_all_holds(hand)

		# then
		assert len(result) == 32

	def test_strategy(self):
		# given
		hand = (1,2,6,6,6)

		# when
		result = strategy(hand, 6)

		# then
		assert result == (20.0, (6,6,6))



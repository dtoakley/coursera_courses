import math
import pytest, unittest
from mock import Mock
from zombie import Apocalypse

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7

class TestClickerState(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.empty_apocalypse = Apocalypse(5, 4)
        self.filled_apocalypse = Apocalypse(5, 4, obstacle_list = [(0,1), (4,2)], \
                                            zombie_list = [(1,0), (4,3)], human_list = [(2,3), (3,2)])

    def test_clear(self):
        # when
        self.filled_apocalypse.clear()

        # then
        assert self.filled_apocalypse.num_zombies() == 0
        assert self.filled_apocalypse.num_humans() == 0
        assert self.filled_apocalypse.is_empty(0,1) is True

    def test_zombies(self):
        # when
        zombies = self.filled_apocalypse.zombies()

        # then
        assert next(zombies) == (1, 0)
        assert next(zombies) == (4, 3)
        with pytest.raises(StopIteration):
            next(zombies)

    def test_humans(self):
        # when
        humans = self.filled_apocalypse.humans()

        # then
        assert next(humans) == (2, 3)
        assert next(humans) == (3, 2)
        with pytest.raises(StopIteration):
            next(humans)

    def test_compute_distance_field(self):
        # when
        zombie_distances = self.filled_apocalypse.compute_distance_field(ZOMBIE)
        human_distances = self.filled_apocalypse.compute_distance_field(HUMAN)

        # then
        assert zombie_distances == [[1, 20, 3, 4], [0, 1, 2, 3], [1, 2, 3, 2], [2, 3, 2, 1], [3, 4, 20, 0]]
        assert human_distances == [[5, 20, 3, 2], [4, 3, 2, 1], [3, 2, 1, 0], [2, 1, 0, 1], [3, 2, 20, 2]]

    def test_move_humans(self):
        # given
        apocalypse = Apocalypse(3, 3, [], [(2, 2)], [(1, 1)])
        human_distance_field = [[4, 3, 2], [3, 2, 1], [2, 1, 0]]

        # when
        apocalypse.move_humans(human_distance_field)
        humans = apocalypse.humans()
        # then
        assert humans.next() == (0, 0)

    def test_move_zombies(self):
        # given
        apocalypse = Apocalypse(3, 3, [(1, 1), (1, 2)], [(2, 2)], [(0, 2)])
        zombie_distance_field = [[2, 1, 0], [3, 9, 9], [4, 5, 6]]

        # when
        apocalypse.move_zombies(zombie_distance_field)
        zombies = apocalypse.zombies()

        # then
        assert zombies.next() == (2, 1)

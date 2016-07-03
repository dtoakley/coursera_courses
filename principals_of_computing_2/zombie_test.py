import math
import pytest, unittest
from mock import Mock
from zombie import Apocalypse

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

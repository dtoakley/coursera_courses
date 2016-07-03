import math
import pytest, unittest
from mock import Mock
from cookie_clicker import ClickerState, simulate_clicker, strategy_cursor_broken, strategy_cheap, strategy_expensive, strategy_best

from poc_clicker_provided import BuildInfo

class TestClickerState(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.clicker_state = ClickerState()
        self.total_cookies = 0.0
        self.current_cookies = 0.0
        self.current_time = 0.0
        self.cps = 1.0
        self.sim_time = 10000000000.0
        self.history = [(0.0, None, 0.0, 0.0)]

    def test_time_until(self):
        # given
        cookies1 = 0
        cookies2 = 10.0
        cookies3 = 0.75
        cookies4 = 1.25

        # when
        time_until1 = self.clicker_state.time_until(cookies1)
        time_until2 = self.clicker_state.time_until(cookies2)
        time_until3 = self.clicker_state.time_until(cookies3)
        time_until4 = self.clicker_state.time_until(cookies4)

        # then
        assert time_until1 == 0.0
        assert time_until2 == 10.0
        assert time_until3 == 1.0
        assert time_until4 == 2.0

    def test_wait_0(self):
        # given
        state_to_check = self.clicker_state

        # when
        self.clicker_state.wait(0.0)

        # then
        assert self.clicker_state == state_to_check


    def test_wait_10(self):
        # when
        self.clicker_state.wait(10.0)

        # then
        assert self.clicker_state.get_cookies() == 10.0
        assert self.clicker_state.get_time() == 10.0

    def test_wait_5_8(self):
        # when
        self.clicker_state.wait(5.8)

        # then
        assert self.clicker_state.get_cookies() == 5.8
        assert self.clicker_state.get_time() == 5.8

    def test_cursor_broken(self):
        # given
        build_info = BuildInfo()

        # when
        clicker_state = simulate_clicker(build_info, self.sim_time, strategy_cursor_broken)
        total_cookies = clicker_state._total_cookies

        # then
        assert clicker_state.get_time() == 10000000000.0
        assert round(clicker_state.get_cookies(), 1) == 6965195661.5
        assert round(clicker_state.get_cps(), 1) == 16.1
        assert math.ceil(total_cookies) == 153308849166.0

    @pytest.mark.parametrize("chosen_item, updated_item, times_updated", [
        ("Cursor", 'Cursor', 0),
        ("Grandma", 'Cursor', 15)
    ])
    def test_strategy_cheap(self, chosen_item, updated_item, times_updated):
        # given
        time_left = 1000.0
        build_info = BuildInfo()
        for x in range(times_updated):
            build_info.update_item(updated_item)

        # when
        result = strategy_cheap(self.current_cookies, self.cps, self.history, time_left, build_info)
        # then
        assert chosen_item == result

    @pytest.mark.parametrize("chosen_item, time_left", [
        ("Cursor", 15.0),
        ("Grandma", 100.0),
        ("Factory", 3000.0),
        ("Antimatter Condenser", 4000000000.0)
    ])
    def test_strategy_expensive(self, chosen_item, time_left):
        # given
        build_info = BuildInfo()

        # when
        result = strategy_expensive(self.current_cookies, self.cps, self.history, time_left, build_info)

        # then
        assert chosen_item == result

    def test_strategy_best(self):
        # given
        build_info = BuildInfo()

        # when
        clicker_state = simulate_clicker(build_info, self.sim_time, strategy_best)

        # then
        print(clicker_state)
        assert clicker_state._total_cookies > 1.3 * 10**18
        assert False

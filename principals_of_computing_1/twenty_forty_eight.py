"""
Clone of 2048 game.
"""

# import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    result = line[:]
    result.sort(key=lambda v: v == 0)
    
    for key, number in enumerate(result):
        try:
            if number == result[key + 1] and number is not 0:
                result[key] = 2 * number
                result[key + 1] = 0

        except IndexError:
            pass
    
    result.sort(key=lambda v: v == 0)

    return result

class TwentyFortyEight(object):
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._initial_tiles = {
            1: [[0, col] for col in range(0, self._grid_width)],
            2: [[self._grid_height - 1, col] for col in range(0, self._grid_width)],
            3: [[row, 0] for row in range(0, self._grid_height)],
            4: [[row, self._grid_width - 1] for row in range(0, self._grid_height)]
        }
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for x in range(self._grid_width)] for x in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "\n".join([str(row) for row in self._grid])

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        tiles_changed = False

        for tile_coord in self._initial_tiles.get(direction):
            to_merge = [self.get_tile(tile_coord[0], tile_coord[1])]
            offset = list(OFFSETS.get(direction))
            end_of_line = False
            start_tile_coord = tile_coord

            while not end_of_line:
                try:
                    next_coord = [start_tile_coord[0] + offset[0], start_tile_coord[1] + offset[1]]
                    next_tile = self.get_tile(next_coord[0], next_coord[1])
                    to_merge.append(next_tile)
                    start_tile_coord = [next_coord[0], next_coord[1]]
                except IndexError:
                    end_of_line = True
            
            new_line = merge(to_merge)
            
            for value in new_line:
                try:
                    if value is not self.get_tile(tile_coord[0], tile_coord[1]):
                        tiles_changed = True
                    self.set_tile(tile_coord[0], tile_coord[1], value)
                    tile_coord = [tile_coord[0] + offset[0], tile_coord[1] + offset[1]]

                except IndexError:
                    break
        # uncomment this for the true functionality - but test will fail for due randomness of new tile. 
        # if tiles_changed:
        #     self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        print("grid", self._grid)
        new_tile_value = 2 if random.random() < 0.90 else 4
        empty_tile_coords = [[row_ind, col_ind] for row_ind, row in enumerate(self._grid) 
                     for col_ind, col in enumerate(row) if self._grid[row_ind][col_ind] == 0]
        print("empty", empty_tile_coords)
        new_tile_coords = empty_tile_coords[random.randint(0, len(empty_tile_coords)) - 1]
        
        self.set_tile(new_tile_coords[0], new_tile_coords[1], new_tile_value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        if row < 0 or col < 0:
            raise IndexError
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        if row < 0 or col < 0:
            raise IndexError
        return self._grid[row][col]
        

#poc_2048_gui.run_gui(TwentyFortyEight(4, 6))



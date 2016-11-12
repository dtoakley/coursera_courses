"""
Loyd"s Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

#import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid is not None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if not self.get_number(target_row, target_col) == 0:
            return False

        for row in range(self.get_height() - 1, target_row, -1):
            for col in range(self.get_width() - 1, -1, -1):
                if self.get_number(row, col) != 0 and (row, col) != self.current_position(row, col):
                    return False

        for col in range(self.get_width() - 1, target_col, -1):            
            if self.get_number(target_row, col) != 0 and (target_row, col) != self.current_position(target_row, col):
                return False

        return True

    def get_move_string(self, target_row, target_col, row, col):
        """
        Builds and returns the move_string
        """
        move_string = ""
        
        row_delta = target_row - row
        col_delta = target_col - col

        move_string += row_delta * "u"

        if col_delta == 0:
            move_string += "ld" + (row_delta - 1) * "druld"
        else:
            if col_delta > 0:
                move_string += col_delta * "l"
                if row == 0:
                    move_string += (abs(col_delta) - 1) * "drrul"
                else:
                    move_string += (abs(col_delta) - 1) * "urrdl"
            elif col_delta < 0:
                move_string += (abs(col_delta) - 1)  * "r"
                if row == 0:
                    move_string += abs(col_delta) * "rdllu"
                else:
                    move_string += abs(col_delta) * "rulld"
            move_string += row_delta * "druld"

        return move_string


    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        row, col = self.current_position(target_row, target_col)
        move_string = self.get_move_string(target_row, target_col, row, col)
        
        self.update_puzzle(move_string)
        
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        
        move_string = "ur"
        self.update_puzzle(move_string)
        row, col = self.current_position(target_row, 0)

        if row == target_row and col == 0:
            move = (self.get_width() - 2) * "r"
            self.update_puzzle(move)
            move_string += move
        else:
            move = self.get_move_string(target_row - 1, 1, row, col)
            move += "ruldrdlurdluurddlu" + (self.get_width() - 1) * "r"
            self.update_puzzle(move)
            move_string += move

        return move_string

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.get_number(0, target_col) == 0:
            return False

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                if (row == 0 and col > target_col) or (row == 1 and col >= target_col) or row > 1:
                    if not (row, col) == self.current_position(row, col):
                        return False

        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.get_number(1, target_col) == 0:
            return False

        for row in range(2, self.get_height()):
            for col in range(self.get_width()):
                if not (row, col) == self.current_position(row, col):
                    return False

        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        move_string = "ld"
        self.update_puzzle(move_string)

        row, col = self.current_position(0, target_col)

        if row == 0 and col == target_col:
            return move_string
        else: 
            move = self.get_move_string(1, target_col - 1, row, col)
            move += "urdlurrdluldrruld"
            self.update_puzzle(move)
            move_string += move

        return move_string

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        row, col = self.current_position(1, target_col)
        move_string = self.get_move_string(1, target_col, row, col)
        move_string += "ur"

        self.update_puzzle(move_string)
        return move_string

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        move_string = ""
        first_move = ""

        if self.get_number(1, 1) == 0:
            first_move += "ul"
            self.update_puzzle(first_move)
            
            if (0, 1) == self.current_position(0, 1) and (1, 1) == self.current_position(1, 1):
                return first_move

            if self.get_number(0, 1) < self.get_number(1, 0):
                move_string += "rdlu"
            else:
                move_string += "drul"        
            self.update_puzzle(move_string)
            
        return first_move + move_string

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        move_string = ""

        row = self.get_height() - 1
        col = self.get_width() - 1
        current_row, current_col = self.current_position(0, 0)
    
        col_delta = current_col - col
        row_delta = current_row - row
        step = abs(col_delta) * "r" + abs(row_delta) * "d"
        self.update_puzzle(step)
        move_string += step

        for temp_row in range(row, 1, -1):
            for temp_col in range(col, 0, -1):
                move_string += self.solve_interior_tile(temp_row, temp_col)
            move_string += self.solve_col0_tile(temp_row)

        for temp_col in range(col, 1, -1):
            move_string += self.solve_row1_tile(temp_col)
            move_string += self.solve_row0_tile(temp_col)

        move_string += self.solve_2x2()
        return move_string

# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))



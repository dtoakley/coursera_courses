"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
#import poc_zombie_gui

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None,
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list is not None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list is not None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list is not None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in range(self.num_zombies()):
            yield self._zombie_list[zombie]

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in range(self.num_humans()):
            yield self._human_list[human]

    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        grid_height = self.get_grid_height()
        grid_width = self.get_grid_width()

        self._visited = poc_grid.Grid(grid_height, grid_width)
        self._distance_field = [[grid_height * grid_width for dummy_col in range(grid_width)]
                       for dummy_row in range(grid_height)]
        self._boundary = poc_queue.Queue()

        if entity_type is ZOMBIE:
            for zombie in self.zombies():
                    self._boundary.enqueue(zombie)
        if entity_type is HUMAN:
            for human in self.humans():
                self._boundary.enqueue(human)

        for entity in self._boundary:
            self._visited.set_full(entity[0], entity[1])
            self._distance_field[entity[0]][entity[1]] = 0

        while len(self._boundary) > 0:
            cell = self._boundary.dequeue()
            distance = self._distance_field[cell[0]][cell[1]]
            neighbours = self._visited.four_neighbors(cell[0], cell[1])

            for neighbour in neighbours:
                row, col = neighbour[0], neighbour[1]
                if self._visited.is_empty(row, col) and self.is_empty(row, col):
                    self._distance_field[row][col] = min(self._distance_field[row][col], distance + 1)
                    self._visited.set_full(row, col)
                    self._boundary.enqueue(neighbour)
        return self._distance_field

    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for human in self.humans():
            human_row, human_col = human[0], human[1]
            current_dist = zombie_distance_field[human_row][human_col]
            neighbours = self.eight_neighbors(human_row, human_col)

            best_position = human
            best_dist = current_dist

            for neighbour in neighbours:
                neigh_row, neigh_col = neighbour[0], neighbour[1]
                neigh_dist = zombie_distance_field[neigh_row][neigh_col]

                if neigh_dist > best_dist and self.is_empty(neigh_row, neigh_col):
                    best_dist = neigh_dist
                    best_position = neighbour

            self._human_list[self._human_list.index(human)] = best_position

    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """

        for zombie in self.zombies():
            zombie_row, zombie_col = zombie[0], zombie[1]
            current_dist = human_distance_field[zombie_row][zombie_col]
            neighbours = self.four_neighbors(zombie_row, zombie_col)

            best_position = zombie
            best_dist = current_dist

            for neighbour in neighbours:
                neigh_row, neigh_col = neighbour[0], neighbour[1]
                neigh_dist = human_distance_field[neigh_row][neigh_col]

                if neigh_dist < best_dist and self.is_empty(neigh_row, neigh_col):
                    best_dist = neigh_dist
                    best_position = neighbour

            self._zombie_list[self._zombie_list.index(zombie)] = best_position

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

# poc_zombie_gui.run_gui(Apocalypse(30, 40))

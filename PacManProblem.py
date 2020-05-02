from collections import deque
from collections import Counter
from search import Problem
from utils import *

# Pre-defined actions for PacManProblem
directions4 = {'W': (0, -1), 'N': (1, 0), 'E': (0, 1), 'S': (-1, 0)}
# Pre-defined grid spots of the PacManProblem
spots = { 
    "initial": 0, # pacman initial position -> traversable
    "pacman": 1, # pacman current spot -> traversable
    "exploring": 2, # search methods current exploring spot -> traversable
    "goal": 3, # goal -> traversable
    "white": 4, # traversable spot
    "grey": 5, # traversable and a collectable item
    "black": 6, # not traversable (wall)
    "ghost": 7 # ghost -> not traversable
}
notTraversable = 6 # spots >= notTraversable arent traversable

class PacManProblem(Problem):
    """Problem of finding an optimal route in a pacman grid, assuming you dont have to get all of the collectable items"""
    """Each grid element can be either by default:
    white = 0 which means its a traversable spot
    grey = 1 which means its a traversable spot and a collectable item 
    black = 2 which means its non traversable
    ghost = 3 which means its not traversable
    """

    def __numberOfItemsInGrid(self):
        return sum([sublist.count(self.defined_spots["grey"]) for sublist in self.grid])

    def __init__(self, initial, goal, grid, defined_actions=directions4, defined_spots=spots):
        """The grid is a 2 dimensional array/list whose state is specified by tuple of indices"""
        super().__init__(initial, goal)
        self.pacman_active = False # only active after signal activePacman()
        self.grid = grid
        self.defined_actions = defined_actions
        self.defined_spots = defined_spots
        self.n = len(grid)
        self.grid[initial[0]][initial[1]] = self.defined_spots["initial"]
        self.grid[goal[0]][goal[1]] = self.defined_spots["goal"]
        assert self.n > 0
        self.m = len(grid[0])
        assert self.m > 0
        self.numberOfItemsInGrid = self.__numberOfItemsInGrid()

    def actions(self, state):
        """Returns the list of actions which are allowed to be taken from the given state"""
        allowed_actions = []
        for action in self.defined_actions:
            next_state = vector_add(state, self.defined_actions[action])
            if 0 <= next_state[0] <= self.n - 1 and 0 <= next_state[1] <= self.m - 1: 
                if self.grid[next_state[0]][next_state[1]] < notTraversable: # traversable
                    allowed_actions.append(action)
        return allowed_actions

    def activate_pacman(self): # signal the class object that the search method got finished and now pacman is traversing
        self.pacman_active = True

    def deactivate_pacman(self): # signal the class object that the search method got finished and now pacman is traversing
        self.pacman_active = False

    def result(self, state, action):
        """Moves in the direction specified by action and remove an item from the grid"""
        next_state = vector_add(state, self.defined_actions[action])

        if (self.pacman_active == True): # we only want to change the grid when the actual pacman walks through it. when we are exploring through a search method, nothings gonna happen
            if (self.grid[state[0]][state[1]] != self.defined_spots["initial"]): # we want to still mark the initial spot on grid to better visualization 
                self.grid[state[0]][state[1]] = self.defined_spots["white"]
            if (self.grid[next_state[0]][next_state[1]] == self.defined_spots["grey"]): # collect item 
                self.numberOfItemsInGrid = self.numberOfItemsInGrid - 1
            self.grid[next_state[0]][next_state[1]] = self.defined_spots["pacman"] 
        
        return next_state

    def value(self, state):
        """Value of a state is the value it is the index to"""
        x, y = state
        assert 0 <= x < self.n
        assert 0 <= y < self.m
        return self.grid[x][y]

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""

        """ depois a gente ve isso
        if (super().goal_test(state) and self.numberOfItemsInGrid == 0): return 1
        return 0
        """
        return super().goal_test(state)

    # implementation of h funcion for A* and greedy_path heuristic  
    def h(self, state):
        return int(distance(state, self.goal))
    
    # implementation of greedy_item heuristic function -> tries to get more items
    def itens_from_root_to_node(self, node):
        counter = 0
        for n in node.path(): # for each node n in the path from root to node
            if self.grid[n.state[0]][n.state[1]] == self.defined_spots["grey"] : # item
                counter = counter + 1
        return counter

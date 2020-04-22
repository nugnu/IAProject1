from PacManProblem import *
from gridVisual import *
import numpy as np

N = 5 # y size
M = 8 # x size
grid =  np.random.randint(3,6, size=(N,M)) # randomize white, grey and black spots
grid = grid.tolist()
initial = (0,0)
goal = (N-1, M-1)
problem = PacManProblem(initial, goal, grid)
problem.grid[2][3] = problem.defined_spots["ghost"]
problem.grid[1][2] = problem.defined_spots["ghost"]
problem.grid[3][7] = problem.defined_spots["ghost"]

print(problem.defined_actions)
print(problem.defined_spots)
print(problem.actions((1,1)))
print(problem.actions((2,2)))
print(problem.grid[3][2], problem.grid[2][3], problem.grid[1][2], problem.grid[2][1]) # (2,2) + N, E, S, W
print(problem.actions((0,24)))
print(problem.numberOfItemsInGrid)
print(problem.result((1,1), "W"))
print(problem.result((1,0), "N"))
print(problem.numberOfItemsInGrid)
print(problem.goal_test((N-1, M-1)))
display_grid(problem)


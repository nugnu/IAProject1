from searchMethods import *
from PacManProblem import *
from gridVisual import *
import numpy as np
from mazegen import *
import os
from glob import glob 

initialValues = [(14,14), (14,14)] 
goalValues= [(14,14), (14,14)]
initialDict= dict(zip(range(len(initialValues)), initialValues)) # 0:initialValues[0], 1:initialValues[1] ...
goalDict= dict(zip(range(len(goalValues)), initialValues)) # 0:goalValues[0], 1:goalValues[1] ...

cwd = os.getcwd()
mazePath = os.path.join(cwd, "mazes/")
defaultMazeExtension = ".in"
mazes = glob(mazePath + "*" + defaultMazeExtension)
problems = []

iterator = 0
for maze in mazes:
    problems.append(PacManProblem(initialDict[iterator], goalDict[iterator], generate_maze(maze)))
    iterator = iterator + 1



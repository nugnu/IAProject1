import networkx as nx                                                                                                                        
import ipywidgets as widgets
from search import Node 
from collections import deque
from gridVisual import assign_node_initial_colors
from gridVisual import assign_color_by_grid_spot
from utils import *

# USED BY BOTH UNINFORMED AND INFORMED METHODS

# can be used by uniform search (uninformed)
# can be used by greed_path, greed_item search and A* (informed heuristics)

def grid_best_first_search(problem, f, order='min'): # Informed search method that uses f function as a heuristic to solve the problem, min_heap by default. 
    # useful variables 
    N = len(problem.grid) # y
    M = len(problem.grid[0]) # x
    G = nx.grid_2d_graph(N,M)

    # we use these two variables at the time of visualisations
    iterations = 0
    all_node_colors = []
    node_colors = assign_node_initial_colors(G.nodes(), problem.grid, problem)
    all_node_colors.append(list(node_colors))
    
    # cache
    f = memoize(f, 'f')

    # Adding first node to the Priority Queue
    frontier = PriorityQueue(order=order, f=f)
    frontier.append(Node(problem.initial))

    # set of explored nodes, to avoid visiting the same nodes over and over  
    explored = set()
    
    while frontier:
        # Popping first node of Priority Queue

        node = frontier.pop()

        node_colors[node.state[0]*M + node.state[1]] = "orange" # current position being explored
        iterations += 1
        all_node_colors.append(list(node_colors))
        node_colors[node.state[0]*M + node.state[1]] = assign_color_by_grid_spot(node.state[0], node.state[1], problem.grid, problem) # get back to the original color on the next iteration

        if problem.goal_test(node.state):
            goal_node = node
            pacman_pos = problem.initial # pacman position after taking action
            pacman_old = problem.initial # pacman position before taking action
            problem.activate_pacman() # signal the object problem that pacman is now traversing 
            for action in goal_node.solution(): # set of actions to go from root to goal
                pacman_old = pacman_pos
                pacman_pos = problem.result(pacman_pos, action) # grid automatically changed after problem.result and the action taken
                node_colors[pacman_pos[0]*M + pacman_pos[1]] = assign_color_by_grid_spot(pacman_pos[0], pacman_pos[1], problem.grid, problem)  # current position being explored
                node_colors[pacman_old[0]*M + pacman_old[1]] = assign_color_by_grid_spot(pacman_old[0], pacman_old[1], problem.grid, problem) 
                iterations += 1
                all_node_colors.append(list(node_colors))
            problem.deactivate_pacman()
            return (iterations, all_node_colors, node)
    
        explored.add(node.state)

        for expandedNode in node.expand(problem):
            if expandedNode.state not in explored and expandedNode not in frontier:
                frontier.append(expandedNode)
            elif expandedNode in frontier: # we have to check if the path to expandedNode got better by checking f function for both nodes 
                if f(expandedNode) < frontier[expandedNode]:
                    del frontier[expandedNode]
                    frontier.append(expandedNode)
        
    return None

# UNINFORMED SEARCH

def grid_breadth_first_search(problem): # BFS
    # useful variables 
    N = len(problem.grid) # y
    M = len(problem.grid[0]) # x
    G = nx.grid_2d_graph(N,M)

    # we use these two variables at the time of visualisations
    iterations = 0
    all_node_colors = []
    node_colors = assign_node_initial_colors(G.nodes(), problem.grid, problem)
    all_node_colors.append(list(node_colors))

    # Adding first node to the queue
    frontier = deque([Node(problem.initial)])
    # set of explored nodes, to avoid visiting the same nodes over and over  
    explored = set()

    while frontier:
        # Popping first node of queue
        node = frontier.popleft()

        node_colors[node.state[0]*M + node.state[1]] = "orange" # current position being explored
        iterations += 1
        all_node_colors.append(list(node_colors))
        node_colors[node.state[0]*M + node.state[1]] = assign_color_by_grid_spot(node.state[0], node.state[1], problem.grid, problem) # get back to the original color on the next iteration

        if problem.goal_test(node.state):
            goal_node = node
            pacman_pos = problem.initial # pacman position after taking action
            pacman_old = problem.initial # pacman position before taking action
            problem.activate_pacman() # signal the object problem that pacman is now traversing 
            for action in goal_node.solution(): # set of actions to go from root to goal
                pacman_old = pacman_pos
                pacman_pos = problem.result(pacman_pos, action) # grid automatically changed after problem.result and the action taken
                node_colors[pacman_pos[0]*M + pacman_pos[1]] = assign_color_by_grid_spot(pacman_pos[0], pacman_pos[1], problem.grid, problem)  # current position being explored
                node_colors[pacman_old[0]*M + pacman_old[1]] = assign_color_by_grid_spot(pacman_old[0], pacman_old[1], problem.grid, problem) 
                iterations += 1
                all_node_colors.append(list(node_colors))
            problem.deactivate_pacman()
            return (iterations, all_node_colors, node)
    
        explored.add(node.state)
        frontier.extend(expandedNode for expandedNode in node.expand(problem)
                        if expandedNode.state not in explored 
                        and expandedNode not in frontier
        )
        
    return None

def grid_depth_first_search(problem): # DFS
    # useful variables 
    N = len(problem.grid) # y
    M = len(problem.grid[0]) # x
    G = nx.grid_2d_graph(N,M)

    # we use these two variables at the time of visualisations
    iterations = 0
    all_node_colors = []
    node_colors = assign_node_initial_colors(G.nodes(), problem.grid, problem)
    all_node_colors.append(list(node_colors))

    # Adding first node to the queue
    frontier = [Node(problem.initial)]
    # set of explored nodes, to avoid visiting the same nodes over and over  
    explored = set()
    
    while frontier:
        # Popping first node of queue
        node = frontier.pop()

        node_colors[node.state[0]*M + node.state[1]] = "orange" # current position being explored
        iterations += 1
        all_node_colors.append(list(node_colors))
        node_colors[node.state[0]*M + node.state[1]] = assign_color_by_grid_spot(node.state[0], node.state[1], problem.grid, problem) # get back to the original color on the next iteration

        if problem.goal_test(node.state):
            goal_node = node
            pacman_pos = problem.initial # pacman position after taking action
            pacman_old = problem.initial # pacman position before taking action
            problem.activate_pacman() # signal the object problem that pacman is now traversing 
            for action in goal_node.solution(): # set of actions to go from root to goal
                pacman_old = pacman_pos
                pacman_pos = problem.result(pacman_pos, action) # grid automatically changed after problem.result and the action taken
                node_colors[pacman_pos[0]*M + pacman_pos[1]] = assign_color_by_grid_spot(pacman_pos[0], pacman_pos[1], problem.grid, problem)  # current position being explored
                node_colors[pacman_old[0]*M + pacman_old[1]] = assign_color_by_grid_spot(pacman_old[0], pacman_old[1], problem.grid, problem) 
                iterations += 1
                all_node_colors.append(list(node_colors))
            problem.deactivate_pacman()
            return (iterations, all_node_colors, node)
    
        explored.add(node.state)
        frontier.extend(expandedNode for expandedNode in node.expand(problem)
                        if expandedNode.state not in explored 
                        and expandedNode not in frontier
        )
                
        
    return None

# uniform cost is best_first_search with f = path_cost
def grid_uniform_cost_search(problem):
    iterations, all_node_colors, node = grid_best_first_search(problem, f = lambda n: n.path_cost)
    return(iterations, all_node_colors, node)

# INFORMED SEARCH 

# take priority to a node with more itens from root to node until it reaches goal
def grid_greedy_itens_search(problem):
    item_heuristic = memoize(problem.itens_from_root_to_node, 'item_heuristic')
    iterations, all_node_colors, node = grid_best_first_search(problem, f = lambda n: item_heuristic(n), order = 'max')
    return(iterations, all_node_colors, node)

# uses heuristic to calculate which node is closest to goal and take this node as priority
def grid_greedy_path_search(problem):
    h = memoize(problem.h, 'h')
    iterations, all_node_colors, node = grid_best_first_search(problem, f = lambda n: h(n.state))
    return(iterations, all_node_colors, node)

# A* (considers both path from root to node and the heuristic to calculate path from node to goal)
def grid_astar_search(problem):
    h = memoize(problem.h, 'h')
    iterations, all_node_colors, node = grid_best_first_search(problem, f = lambda n: n.path_cost + h(n.state))
    return(iterations, all_node_colors, node)



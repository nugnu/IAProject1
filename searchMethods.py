import networkx as nx                                                                                                                        
import ipywidgets as widgets
from search import Node 
from collections import deque
from gridVisual import assign_node_initial_colors
from gridVisual import assign_color_by_grid_spot


def grid_breadth_first_tree_search(problem): # BFS
    # useful variables 
    N = len(problem.grid) # y
    M = len(problem.grid[0]) # x
    G = nx.grid_2d_graph(N,M)

    # we use these two variables at the time of visualisations
    iterations = 0
    all_node_colors = []
    node_colors = assign_node_initial_colors(G.nodes(), problem.grid, problem)
    all_node_colors.append(node_colors)

    # Adding first node to the queue
    frontier = deque([Node(problem.initial)])
    
    while frontier:
        # Popping first node of queue
        node = frontier.popleft()

        node_colors[node.state[0]*M + node.state[1]] = "orange" # current position being explored
        iterations += 1
        all_node_colors.append(node_colors)
        node_colors[node.state[0]*M + node.state[1]] = assign_color_by_grid_spot(node.state[0], node.state[1], problem.grid, problem) # get back to the original color on the next iteration

        if problem.goal_test(node.state):
            goal_node = node
            pacman_pos = problem.initial # pacman position after taking action
            pacman_old = problem.initial # pacman position before taking action
            for action in goal_node.solution(): # set of actions to go from root to goal
                pacman_old = pacman_pos
                pacman_pos = problem.result(pacman_pos, action) # grid automatically changed after problem.result and the action taken
                node_colors[pacman_pos[0]*M + pacman_pos[1]] = assign_color_by_grid_spot(pacman_pos[0], pacman_pos[1], problem.grid, problem)  # current position being explored
                node_colors[pacman_old[0]*M + pacman_old[1]] = assign_color_by_grid_spot(pacman_old[0], pacman_old[1], problem.grid, problem) 
                iterations += 1
                all_node_colors.append(node_colors)
            return (iterations, all_node_colors, node)
        
        frontier.extend(node.expand(problem))
        
    return None

def grid_depth_first_tree_search(problem): # DFS
    # useful variables 
    N = len(problem.grid) # y
    M = len(problem.grid[0]) # x
    G = nx.grid_2d_graph(N,M)

    # we use these two variables at the time of visualisations
    iterations = 0
    all_node_colors = []
    node_colors = assign_node_initial_colors(G.nodes(), problem.grid, problem)
    all_node_colors.append(node_colors)

    # Adding first node to the stack
    frontier = [Node(problem.initial)] # STACK
    
    while frontier:
        # Popping first node of stack
        node = frontier.pop()

        node_colors[node.state[0]*M + node.state[1]] = "orange" # current position being explored
        iterations += 1
        all_node_colors.append(node_colors)
        node_colors[node.state[0]*M + node.state[1]] = assign_color_by_grid_spot(node.state[0], node.state[1], problem.grid, problem) # get back to the original color on the next iteration

        if problem.goal_test(node.state):
            goal_node = node
            pacman_pos = problem.initial # pacman position after taking action
            pacman_old = problem.initial # pacman position before taking action
            for action in goal_node.solution(): # set of actions to go from root to goal
                pacman_old = pacman_pos
                pacman_pos = problem.result(pacman_pos, action) # grid automatically changed after problem.result and the action taken
                node_colors[pacman_pos[0]*M + pacman_pos[1]] = assign_color_by_grid_spot(pacman_pos[0], pacman_pos[1], problem.grid, problem)  # current position being explored
                node_colors[pacman_old[0]*M + pacman_old[1]] = assign_color_by_grid_spot(pacman_old[0], pacman_old[1], problem.grid, problem) 
                iterations += 1
                all_node_colors.append(node_colors)
            return (iterations, all_node_colors, node)
        
        frontier.extend(node.expand(problem))
        
    return None


import networkx as nx                                                                                                                        
import matplotlib.pyplot as plt      
import matplotlib.lines as lines     
import ipywidgets as widgets
from IPython.display import display
from collections import deque
import numpy as np

def assign_color_by_grid_spot(y, x, grid, problem):
    val = grid[y][x]
    retColor = None
    if (val==problem.defined_spots["white"]):
        retColor = "white"
    elif (val==problem.defined_spots["grey"]):
        retColor = "grey"
    elif (val==problem.defined_spots["black"]):
        retColor = "black"
    elif (val==problem.defined_spots["ghost"]):
        retColor = "purple"
    elif (val==problem.defined_spots["initial"]):
        retColor = "red"
    elif (val==problem.defined_spots["pacman"]):
        retColor = "yellow"
    elif (val==problem.defined_spots["goal"]):
        retColor = "green"
    elif (val==problem.defined_spots["exploring"]):
        retColor = "orange"
    else: assert 0
    return retColor

def assign_node_initial_colors(nodes, grid, problem):
    node_colors = []
    for node in nodes:
        node_colors.append(assign_color_by_grid_spot(node[0], node[1], grid, problem))
    return node_colors

def show_grid(problem, node_colors = None):
    grid = problem.grid
    N = len(grid) # y
    M = len(grid[0]) # x
    G=nx.grid_2d_graph(N,M)
    if (node_colors == None):
        node_colors = assign_node_initial_colors(G.nodes(), grid, problem)
    pos = dict(zip(G.nodes(),G.nodes()))
    flipped_pos = {node: (y,x) for (node, (x,y)) in pos.items() }
    labels = dict(zip(pos, pos))                              
    nx.draw_networkx(G, pos=flipped_pos, with_labels=True, node_size = 400*50/(N*M), node_color=node_colors)                                                                       
    plt.axis('off')                       
    white_circle = lines.Line2D([], [], color="black", marker='o', markersize=10, markerfacecolor="white")
    grey_circle = lines.Line2D([], [], color="grey", marker='o', markersize=10, markerfacecolor="grey")
    black_circle = lines.Line2D([], [], color="black", marker='o', markersize=10, markerfacecolor="black")
    purple_circle = lines.Line2D([], [], color="purple", marker='o', markersize=10, markerfacecolor="purple")
    red_circle = lines.Line2D([], [], color="red", marker='o', markersize=10, markerfacecolor="red")
    yellow_circle = lines.Line2D([], [], color="yellow", marker='o', markersize=10, markerfacecolor="yellow")
    green_circle = lines.Line2D([], [], color="green", marker='o', markersize=10, markerfacecolor="green")
    orange_circle = lines.Line2D([], [], color="orange", marker='o', markersize=10, markerfacecolor="orange")

    plt.legend((white_circle, grey_circle, black_circle, purple_circle, red_circle, yellow_circle, green_circle, orange_circle),
               ('Traversable Area', 'Item', 'Wall', 'Ghost', 'Initial Position', 'Pacman Current Position', "Goal", "Currently Exploring"),
               numpoints=1, prop={'size': 7}, loc=(-.1, -.1))       
    plt.savefig("grid.png")
    plt.show()
    plt.close()

def display_grid_algorithm(algorithm=None, problem=None):
    
    def slider_callback(iteration):
        # don't show graph for the first time running the cell calling this function
        try:
            printVar = np.array(all_node_colors[iteration]).reshape(len(problem.grid),len(problem.grid[0]))
            print(printVar)
            show_grid(problem, node_colors=all_node_colors[iteration])
        except:
            pass

    def visualize_callback(Visualize):
        if Visualize is True:
            button.value = False

            global all_node_colors

            iterations, all_node_colors, node = algorithm(problem)
            slider.max = len(all_node_colors) - 1


    slider = widgets.IntSlider(min=0, max=1, step=1, value=0)
    slider_visual = widgets.interactive(slider_callback, iteration=slider)
    display(slider_visual)

    button = widgets.ToggleButton(value=False)
    button_visual = widgets.interactive(visualize_callback, Visualize=button)
    display(button_visual)
                                



import networkx as nx                                                                                                                        
import matplotlib.pyplot as plt      
import matplotlib.lines as lines                                                 


def display_grid(problem):
    grid = problem.grid
    N = len(grid) # y
    M = len(grid[0]) # x
    G=nx.grid_2d_graph(N,M)
    node_colors = []
    for node in G.nodes():
        if (grid[node[0]][node[1]]==problem.defined_spots["white"]):
            node_colors.append("white")
        elif (grid[node[0]][node[1]]==problem.defined_spots["grey"]):
            node_colors.append("grey")
        elif (grid[node[0]][node[1]]==problem.defined_spots["black"]):
            node_colors.append("black")
        elif (grid[node[0]][node[1]]==problem.defined_spots["ghost"]):
            node_colors.append("purple")
        elif (grid[node[0]][node[1]]==problem.defined_spots["initial"]):
            node_colors.append("red")
        elif (grid[node[0]][node[1]]==problem.defined_spots["pacman"]):
            node_colors.append("yellow")
        elif (grid[node[0]][node[1]]==problem.defined_spots["goal"]):
            node_colors.append("green")
        else: assert 0
        

    pos = dict(zip(G.nodes(),G.nodes()))
    labels = dict(zip(pos, pos))                              
    nx.draw_networkx(G, pos=pos, with_labels=False, node_size = 400, node_color=node_colors)                                                                       
    nx.draw_networkx_labels(G, pos=pos, labels=labels, font_size=10)                              
    plt.axis('off')                       
    white_circle = lines.Line2D([], [], color="black", marker='o', markersize=10, markerfacecolor="white")
    grey_circle = lines.Line2D([], [], color="grey", marker='o', markersize=10, markerfacecolor="grey")
    black_circle = lines.Line2D([], [], color="black", marker='o', markersize=10, markerfacecolor="black")
    purple_circle = lines.Line2D([], [], color="purple", marker='o', markersize=10, markerfacecolor="purple")
    red_circle = lines.Line2D([], [], color="red", marker='o', markersize=10, markerfacecolor="red")
    yellow_circle = lines.Line2D([], [], color="yellow", marker='o', markersize=10, markerfacecolor="yellow")
    green_circle = lines.Line2D([], [], color="green", marker='o', markersize=10, markerfacecolor="green")
    plt.legend((white_circle, grey_circle, black_circle, purple_circle, red_circle, yellow_circle, green_circle),
               ('Traversable Area', 'Item', 'Wall', 'Ghost', 'Initial Position', 'Pacman Current Position', "Goal"),
               numpoints=1, prop={'size': 7}, loc=(-.1, -.1))       
    plt.savefig("test.png")
    plt.show()
    plt.close()
                                



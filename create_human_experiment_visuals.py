from itertools import product

import math
import networkx as nx
import matplotlib.pyplot as plt

# Create all not connected graphs

two_color_options = ['blue', 'red']
two_color_map_options = list(product(two_color_options, repeat=6))

three_color_options = ['blue', 'red', 'green']
three_color_map_options = list(product(three_color_options, repeat=6))

# Create an empty graph
G = nx.Graph()

# Add six nodes to the graph
G.add_nodes_from([0, 1, 2, 3, 4, 5,])

# Add edges to connect one node to all other nodes
for i in range(1, 6):
    G.add_edge(0, i)

# Define the node positions
# pos = {0: (0, 0), 1: (0, 1), 2: (1, 0.25), 3: (0.5, -1), 4: (-0.5, -1), 5: (-1, 0.25)}
c1 = math.cos(2*math.pi/5)
c2 = math.cos(math.pi/5)
s1 = math.sin(2*math.pi/5)
s2 = math.sin(4*math.pi/5)
pos = {0: (0, 0), 1: (0, 1), 2: (s1, c1), 3: (s2, -c2), 4: (-s2, -c2), 5: (-s1, c1)}

for color_map_option in two_color_map_options:

    plt.clf()

    # Draw the graph
    nx.draw(G, pos=pos, with_labels=False, node_color=[color_map_option[node] for node in G.nodes()], node_size=1000)

    # Save the graph
    color_code = "".join([color[0] for color in color_map_option])
    plt.savefig("./human_experiment_visuals/two_not_connected/human_experiment_visual_%s.png" % color_code)

for color_map_option in three_color_map_options:

    plt.clf()

    # Draw the graph
    nx.draw(G, pos=pos, with_labels=False, node_color=[color_map_option[node] for node in G.nodes()], node_size=1000)

    # Save the graph
    color_code = "".join([color[0] for color in color_map_option])
    plt.savefig("./human_experiment_visuals/three_not_connected/human_experiment_visual_%s.png" % color_code)

for i in range(1, 5):
    G.add_edge(i, i+1)
G.add_edge(5, 1)

for color_map_option in two_color_map_options:

    plt.clf()

    # Draw the graph
    nx.draw(G, pos=pos, with_labels=False, node_color=[color_map_option[node] for node in G.nodes()], node_size=1000)

    # Save the graph
    color_code = "".join([color[0] for color in color_map_option])
    plt.savefig("./human_experiment_visuals/two_connected/human_experiment_visual_%s.png" % color_code)

for color_map_option in three_color_map_options:

    plt.clf()

    # Draw the graph
    nx.draw(G, pos=pos, with_labels=False, node_color=[color_map_option[node] for node in G.nodes()], node_size=1000)

    # Save the graph
    color_code = "".join([color[0] for color in color_map_option])
    plt.savefig("./human_experiment_visuals/three_connected/human_experiment_visual_%s.png" % color_code)
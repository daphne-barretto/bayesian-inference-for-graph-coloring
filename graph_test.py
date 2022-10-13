# %% Imports

from datetime import date
from enum import Enum

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import random

# %% Create Color Enum

class Color(Enum):
    NONE    = "none"
    RED     = 0
    GREEN   = 1
    BLUE    = 2
    YELLOW  = 3
    ORANGE  = 4
    PURPLE  = 5
    PINK    = 6
    GRAY    = 7
    BROWN   = 8
    BLACK   = 9
    
# %% Set trial parameters
trial_num_nodes = 9 # Can vary from 2+
trial_num_colors = 10 # Can currently range from 2-10

# %% Set up graph

G = nx.Graph()
G.add_nodes_from(np.arange(0, trial_num_nodes, 1, dtype=int))
G.add_edges_from([(1,2), (3, 4), (2,5), (4, 5), (6,7), (8,9), (4,7), (1,7), (3,5), (2,7), (5,8), (2,9), (5,7)])
 
# %%

def update_color_history(trial_node_colors, trial_node_color_history):
    for i in range(trial_num_nodes):
        node_i_curr_color_value = Color(trial_node_colors[i]).value
        trial_node_color_history[i][node_i_curr_color_value] += 1

# %%

trial_node_colors = list(np.random.randint(low = 1,high = trial_num_colors, size = trial_num_nodes))
trial_stubborness_quotient = list(np.random.uniform(low = 0.0, high = 1.0, size = trial_num_nodes))
print(trial_stubborness_quotient)
trial_node_color_history = np.zeros((trial_num_nodes, trial_num_colors), dtype=int)

color_map = []
for index, node in enumerate(G):
    color_map.append(Color(trial_node_colors[index]).name)

nx.draw(G, node_color=color_map, with_labels=True)

adjacency_matrix = nx.to_numpy_array(G)
print(adjacency_matrix)
# %%

pos = nx.spring_layout(G)
# %%

def animate(frame):
    
    # print(trial_node_color_history)
    fig.clear()
    # trial_node_colors = list(np.random.randint(low = 1,high = trial_num_colors, size = trial_num_nodes))
    
    print(trial_node_colors)
    for i in range(trial_num_nodes):
        stubborn = random.random() < trial_stubborness_quotient[i]
        if not stubborn:
            neighbor_trial_node_color_history = trial_node_color_history * adjacency_matrix[i].reshape((trial_num_nodes, 1))
            if trial_node_color_history.sum() > 0:
                print("TEST", trial_node_color_history, adjacency_matrix[i], neighbor_trial_node_color_history)
            neighbor_column_color_counts = np.sum(neighbor_trial_node_color_history, axis = 0)
            columns_with_most_instances = np.argwhere(neighbor_column_color_counts == np.amax(neighbor_column_color_counts))
            random_column_with_most_instances = random.choice(columns_with_most_instances)[0]
            # print(random_column_with_most_instances)
            next_color = Color(random_column_with_most_instances).value
            trial_node_colors[i] = next_color
    
    update_color_history(trial_node_colors, trial_node_color_history)
    color_map = []
    for index, node in enumerate(G):
        color_map.append(Color(trial_node_colors[index]).name)
    nx.draw_networkx(G, pos=pos, node_color=color_map, with_labels=True)

    ax = plt.gca()
    ax.set_title("Time " + str(frame))
    
# %%
def init():
    pass

# %%

trial_node_colors = list(np.random.randint(low = 1,high = trial_num_colors, size = trial_num_nodes))
fig = plt.figure()
ani = animation.FuncAnimation(fig, animate, frames=6, interval=1000, repeat=False, init_func=init)

# Save animation
today = date.today().isoformat()
file_index = 0
while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
    file_index += 1
file_name = "./data/animations/animation_" + today + "_" + str(file_index) + ".gif"
ani.save(file_name)

plt.show()
print(trial_node_color_history)
# %%

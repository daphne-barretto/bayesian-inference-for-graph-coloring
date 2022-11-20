# %% Imports

from datetime import date

import argparse
import csv
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import random

today = date.today().isoformat()
file_index = 0
while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
    file_index += 1

csv_file = open("./data/csv/csv_" + today + "_" + str(file_index) + ".csv", "w")
writer = csv.writer(csv_file)

# %% Set initial trial parameters

parser = argparse.ArgumentParser()
parser.add_argument("--is_consensus_not_unique_coloring", type=bool, default=True)
parser.add_argument("--is_consensus_probability_matching", type=bool, default=True)
parser.add_argument("--memory", type=int, default=0)
parser.add_argument("--max_iterations", type=int, default=60)
parser.add_argument("--trial_num_cliques", type=int, default=6)
parser.add_argument("--trial_num_nodes_per_clique", type=int, default=6)
parser.add_argument("--trial_num_colors", type=int, default=9)
parser.add_argument("--trial_stubborness_quotient_low", type=float, default=0.0)
parser.add_argument("--trial_stubborness_quotient_high", type=float, default=0.0)
parser.add_argument("--q", type=float, default=0)
args = vars(parser.parse_args())

is_consensus_not_unique_coloring = args["is_consensus_not_unique_coloring"]
is_consensus_probability_matching = args["is_consensus_probability_matching"]
memory = args["memory"]
max_iterations = args["max_iterations"]

trial_num_cliques = args["trial_num_cliques"]
trial_num_nodes_per_clique = args["trial_num_nodes_per_clique"]
trial_num_colors = args["trial_num_colors"]
trial_stubborness_quotient_low = args["trial_stubborness_quotient_low"]
trial_stubborness_quotient_high = args["trial_stubborness_quotient_high"]
q = args["q"]

writer.writerow(args.keys())
writer.writerow(args.values())

# Calculate trial parameters

trial_num_nodes = trial_num_cliques * trial_num_nodes_per_clique
trial_stubborness_quotient = list(np.random.uniform(low=trial_stubborness_quotient_low, high=trial_stubborness_quotient_high, size=trial_num_nodes))

writer.writerow(trial_stubborness_quotient)
writer.writerow("")

trial_edges_in_clique_1 = []
for i in range(trial_num_nodes_per_clique):
    for j in range(trial_num_nodes_per_clique - i - 1):
        trial_edges_in_clique_1.append((i+1, i+j+2))
trial_num_edges_in_clique = len(trial_edges_in_clique_1) # alternatively, n(n-1)/2

# %% Set up graph

cliques = []
for clique_i in range(trial_num_cliques):
    G = nx.complete_graph(n=trial_num_nodes_per_clique)
    G = nx.convert_node_labels_to_integers(G, first_label=1+trial_num_nodes_per_clique*clique_i, ordering='default', label_attribute=None)
    cliques.append(G)

G = nx.compose_all(cliques)

connectors_edges = []
for i in range(trial_num_cliques - 1):
    a = i * trial_num_nodes_per_clique + 1
    b = a + trial_num_nodes_per_clique
    connectors_edges.append((a, b))

for clique_i in range(trial_num_cliques):
    for edge_i in trial_edges_in_clique_1:
        rewire = random.random() < q
        if rewire:
            old_edge_a = trial_num_nodes_per_clique*clique_i+edge_i[0]
            old_edge_b = trial_num_nodes_per_clique*clique_i+edge_i[1]
            G.remove_edge(old_edge_a, old_edge_b)

            keep_a = random.random() < 0.5
            new_edge_a = old_edge_a if keep_a else old_edge_b
            new_edge_b = new_edge_a
            while(new_edge_a == new_edge_b or G.has_edge(new_edge_a, new_edge_b) or (new_edge_a, new_edge_b) in connectors_edges):
                new_edge_b = random.randint(1, trial_num_nodes)
            G.add_edge(new_edge_a, new_edge_b)

            print("replacing", (old_edge_a, old_edge_b), "with", (new_edge_a, new_edge_b))

G.add_edges_from(connectors_edges)

if not nx.is_connected(G):
    print("Graph is not connected, ending trial...")
    exit()

# %% adjacency_matrix

adjacency_matrix = nx.to_numpy_array(G)
print("adjacenty_matrix", adjacency_matrix)
writer.writerow(adjacency_matrix.tolist())

# %% update_color_history()

def update_color_history(trial_node_colors, trial_node_color_history_counts):
    for i in range(trial_num_nodes):
        node_i_curr_color_value = trial_node_colors[i]
        trial_node_color_history_counts[i][node_i_curr_color_value] += 1
    if len(trial_node_color_history) - 1 > memory:
        for i in range(trial_num_nodes):
            color_to_remove = trial_node_color_history[-(memory+1)][i]
            trial_node_color_history_counts[i][color_to_remove] -= 1

    print("update_color_history(): trial_node_color_history_counts")
    print(trial_node_color_history_counts)
    print("end of update_color_history()")

# %%

# Initialize node colors and node color history
trial_node_colors = list(np.random.randint(low = 0, high = trial_num_colors, size = trial_num_nodes))
trial_node_color_history_counts = np.zeros((trial_num_nodes, trial_num_colors), dtype=int)
trial_node_color_history = []

biggest_component_color_history = []
biggest_component_proportion_history = []
component_proportion_history = []

# Initialize color history and draw initial colored Graph 
color_history = []
for index in range(trial_num_nodes):
    color_history.append(trial_node_colors[index])
trial_node_color_history.append(color_history)

trial_node_colors_bincount = np.bincount(trial_node_colors, minlength=trial_num_colors)
biggest_component_color_history.append(np.argmax(trial_node_colors_bincount))
biggest_component_proportion_history.append(np.max(trial_node_colors_bincount)/trial_num_nodes)
component_proportion_history.append([(x/trial_num_nodes) for x in trial_node_colors_bincount])

# %% run() and run until done

def run_consensus(iteration):
    if iteration == 0 and trial_node_colors.count(trial_node_colors[0]) == len(trial_node_colors):
        return iteration, trial_node_colors.count(trial_node_colors[0]) == len(trial_node_colors)

    for i in range(trial_num_nodes):
        stubborn = random.random() < trial_stubborness_quotient[i]
        if not stubborn:
            if is_consensus_probability_matching:
                neighbor_trial_node_color_history = trial_node_color_history_counts * adjacency_matrix[i].reshape((trial_num_nodes, 1))
                neighbor_trial_node_color_history_no_zeroes = np.asarray([x+1 for x in neighbor_trial_node_color_history])
                neighbor_trial_node_color_probability = neighbor_trial_node_color_history_no_zeroes/(iteration+1+trial_num_colors)
                neighbor_column_node_color_probability = np.prod(neighbor_trial_node_color_probability, axis = 0)
                neighbor_column_node_color_probability_normalized = neighbor_column_node_color_probability / sum(neighbor_column_node_color_probability)
                print(neighbor_column_node_color_probability_normalized)
                probability_matching_column = np.random.choice(np.arange(trial_num_colors), p=neighbor_column_node_color_probability_normalized)
                next_color = probability_matching_column
                trial_node_colors[i] = next_color
            else:
                neighbor_trial_node_color_history = trial_node_color_history_counts * adjacency_matrix[i].reshape((trial_num_nodes, 1))
                neighbor_trial_node_color_history_no_zeroes = np.asarray([x+1 for x in neighbor_trial_node_color_history])
                neighbor_trial_node_color_probability = neighbor_trial_node_color_history_no_zeroes/(iteration+1+trial_num_colors)
                neighbor_column_node_color_probability = np.prod(neighbor_trial_node_color_probability, axis = 0)
                columns_with_highest_probability = np.argwhere(neighbor_column_node_color_probability == np.amax(neighbor_column_node_color_probability))
                random_column_with_highest_probability = random.choice(columns_with_highest_probability)
                next_color = random_column_with_highest_probability[0]
                trial_node_colors[i] = next_color

    update_color_history(trial_node_colors, trial_node_color_history_counts)

    color_history = []
    for index in range(trial_num_nodes):
        color_history.append(trial_node_colors[index])
    trial_node_color_history.append(color_history)

    trial_node_colors_bincount = np.bincount(trial_node_colors, minlength=trial_num_colors)
    biggest_component_color_history.append(np.argmax(trial_node_colors_bincount))
    biggest_component_proportion_history.append(np.max(trial_node_colors_bincount)/trial_num_nodes)
    component_proportion_history.append([(x/trial_num_nodes) for x in trial_node_colors_bincount])

    return iteration + 1, trial_node_colors.count(trial_node_colors[0]) == len(trial_node_colors)

def run_unique_coloring(iteration):
    for i in range(trial_num_nodes):
        stubborn = random.random() < trial_stubborness_quotient[i]
        if not stubborn:
            neighbor_trial_node_color_history = trial_node_color_history_counts * adjacency_matrix[i].reshape((trial_num_nodes, 1))
            neighbor_trial_node_color_history_no_zeroes = np.asarray([x+1 for x in neighbor_trial_node_color_history])
            neighbor_trial_node_color_probability = neighbor_trial_node_color_history_no_zeroes/(iteration+1+trial_num_colors)
            neighbor_column_node_color_probability = np.prod([1-x for x in neighbor_trial_node_color_probability], axis = 0)
            columns_with_highest_probability = np.argwhere(neighbor_column_node_color_probability == np.amax(neighbor_column_node_color_probability))
            random_column_with_highest_probability = random.choice(columns_with_highest_probability)
            next_color = random_column_with_highest_probability[0]
            trial_node_colors[i] = next_color

    update_color_history(trial_node_colors, trial_node_color_history_counts)

    color_history = []
    for index in range(trial_num_nodes):
        color_history.append(trial_node_colors[index])
    trial_node_color_history.append(color_history)

    trial_node_colors_bincount = np.bincount(trial_node_colors, minlength=trial_num_colors)
    biggest_component_color_history.append(np.argmax(trial_node_colors_bincount))
    biggest_component_proportion_history.append(np.max(trial_node_colors_bincount)/trial_num_nodes)
    component_proportion_history.append([(x/trial_num_nodes) for x in trial_node_colors_bincount])

    next_iteration = iteration + 1
    graph_coloring_complete = check_graph_coloring(trial_node_colors)

    return next_iteration, graph_coloring_complete

# %%

def check_graph_coloring(trial_node_colors):
    for edge in G.edges():
        if trial_node_colors[edge[0]] == trial_node_colors[edge[1]]:
            return False
    return True

# %%

iteration = 0
done = False
if is_consensus_not_unique_coloring:
    while iteration < max_iterations and not done: 
        iteration, done = run_consensus(iteration)
else:
    while iteration < max_iterations and not done: 
        iteration, done = run_unique_coloring(iteration)

print(trial_node_color_history)

# %%
print(biggest_component_color_history)
print(biggest_component_proportion_history)

writer.writerow(trial_node_color_history)
writer.writerow(trial_node_color_history_counts)
writer.writerow(biggest_component_color_history)
writer.writerow(biggest_component_proportion_history)
writer.writerow("")
writer.writerow([done, iteration, biggest_component_proportion_history[-1]])
writer.writerow("TESTING")
writer.writerow(component_proportion_history)

# %% animate()

# default_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
default_colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

def animate(frame):
    ax = plt.gca()
    ax.set_title("Time " + str(frame))
    # nc = [default_colors[x] for x in trial_node_color_history[frame]]
    nc = trial_node_color_history[frame]
    print("PRINTING NODE COLORS")
    print(nc)
    nodes.set_array(nc)
    return nodes,

# %% layout and draw graph

pos = nx.spring_layout(G)
nodes = nx.draw_networkx_nodes(G, pos, cmap="tab10", node_color=range(trial_num_nodes))
edges = nx.draw_networkx_edges(G, pos)
edges = nx.draw_networkx_labels(G, pos)
plt.axis('off')

fig = plt.gcf()
ani = animation.FuncAnimation(fig, animate, interval=500, frames=iteration+1, blit=True)

file_name = "./data/animations/animation_" + today + "_" + str(file_index) + ".gif"
ani.save(file_name)

csv_file.close()

biggest_component_plot_file = "./data/biggest_component_plot/biggest_component_plot_" + today + "_" + str(file_index) + ".png"

plt.clf()
plt.title(today + "_" + str(file_index) + ", " + str(biggest_component_proportion_history[-1]))
# plt.scatter(np.arange(len(biggest_component_proportion_history)), biggest_component_proportion_history, c=biggest_component_color_history, s=6)
component_proportion_history = np.array(component_proportion_history)
print(component_proportion_history)

for i in range(trial_num_colors):
    plt.plot(component_proportion_history[:,i])


plt.savefig(biggest_component_plot_file)
print("POST SAVE")
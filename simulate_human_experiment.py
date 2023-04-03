from itertools import product

import csv
import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

def simulate_deterministic_theory_of_mind(num_colors, color_map, color_code, K=0, csv_file_writer=None, iterations=1):
    num_nodes = len(color_map)
    adjacency_matrix = nx.to_numpy_array(G, dtype=bool)

    num_color_choice_per_K = np.zeros((K+1, num_colors), dtype=int)
    csv_data = [color_code, "K=%d" % K, "iterations=%d" % iterations]
    for _ in range(iterations):
        current_node_colors = color_map.copy()
        for K_iteration in range(K+1):
            current_node_colors_copy = current_node_colors.copy()
            for i in range(num_nodes):
                current_neighbor_colors = np.array(current_node_colors_copy)[adjacency_matrix[i]]
                current_neighbor_colors_count = np.bincount(current_neighbor_colors)
                current_node_colors_most_neighbors = [i for i, x in enumerate(current_neighbor_colors_count) if x == max(current_neighbor_colors_count)]
                current_node_colors[i] = random.choice(current_node_colors_most_neighbors)
                # print(current_node_colors_copy, adjacency_matrix[i], current_neighbor_colors, current_neighbor_colors_count, current_node_colors_most_neighbors, current_node_colors[i])
            num_color_choice_per_K[K_iteration][current_node_colors[0]-1] += 1
    csv_data.append(num_color_choice_per_K.tolist())
    K_0_not_equal_K_1 = not np.all(num_color_choice_per_K[0] == num_color_choice_per_K[1])
    K_0_not_equal_K_1_deterministic = any((num_color_choice_per_K[0][i] == iterations and num_color_choice_per_K[1][i] == 0) or (num_color_choice_per_K[0][i] == 0 and num_color_choice_per_K[1][i] == iterations) for i in range(len(num_color_choice_per_K[0])))
    csv_data.append(K_0_not_equal_K_1)
    csv_data.append(K_0_not_equal_K_1_deterministic)
    if csv_file_writer is not None:
       csv_file_writer.writerow(csv_data) 
    return K_0_not_equal_K_1, K_0_not_equal_K_1_deterministic

if __name__ == '__main__':

    csv_file_connected = open("./human_experiment_simulation_data/three_connected.csv", "w")
    writer_connected = csv.writer(csv_file_connected)
    csv_file_not_connected = open("./human_experiment_simulation_data/three_not_connected.csv", "w")
    writer_not_connected = csv.writer(csv_file_not_connected)

    two_color_options = [1, 2]
    two_color_map_options = list(product(two_color_options, repeat=6))

    three_color_options = [1, 2, 3]
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

    # for color_map_option in two_color_map_options:
    #     color_map = np.array(color_map_option).copy()
    #     color_map_option = list(np.array(color_map_option).copy())
    #     for i in range(len(color_map_option)):
    #         color_map_option[i] = 'red' if color_map_option[i] == 1 else ('blue' if color_map_option[i] == 2 else 'green')

    #     plt.clf()

    #     # Draw the graph
    #     nx.draw(G, pos=pos, with_labels=False, node_color=[color_map_option[node] for node in G.nodes()], node_size=1000)

    #     plt.annotate("You", xy=pos[0], xytext=(20, -10), textcoords='offset points', ha='left', va='center', fontsize=16, color='black', fontweight='bold')

    #     # Save the graph
    #     color_code = "".join([color[0] for color in color_map_option])
    #     plt.savefig("./human_experiment_visuals/two_not_connected/human_experiment_visual_%s.png" % color_code)
    #     simulate_deterministic_theory_of_mind(color_map, K=2)

    color_codes_where_K_0_not_equal_K_1 = []
    color_codes_where_K_0_not_equal_K_1_deterministic = []
    for color_map_option in three_color_map_options:
        color_map = np.array(color_map_option).copy()
        color_map_option = list(np.array(color_map_option).copy())
        for i in range(len(color_map_option)):
            color_map_option[i] = 'red' if color_map_option[i] == 1 else ('blue' if color_map_option[i] == 2 else 'green')
        color_code = "".join([color[0] for color in color_map_option])

        # plt.clf()
        # nx.draw(G, pos=pos, with_labels=False, node_color=[color_map_option[node] for node in G.nodes()], node_size=1000)
        # plt.annotate("You", xy=pos[0], xytext=(20, -10), textcoords='offset points', ha='left', va='center', fontsize=16, color='black', fontweight='bold')
        # plt.savefig("./human_experiment_visuals/three_not_connected/human_experiment_visual_%s.png" % color_code)
        
        K_0_not_equal_K_1, K_0_not_equal_K_1_deterministic = simulate_deterministic_theory_of_mind(3, color_map, color_code, K=1, csv_file_writer=writer_not_connected, iterations=1000)
        if K_0_not_equal_K_1:
            color_codes_where_K_0_not_equal_K_1.append(color_code)
        if K_0_not_equal_K_1_deterministic:
            color_codes_where_K_0_not_equal_K_1_deterministic.append(color_code)

    writer_not_connected.writerow([len(color_codes_where_K_0_not_equal_K_1), color_codes_where_K_0_not_equal_K_1])
    color_codes_where_K_0_not_equal_K_1_no_g = [color_code for color_code in color_codes_where_K_0_not_equal_K_1 if 'g' not in color_code]
    writer_not_connected.writerow([len(color_codes_where_K_0_not_equal_K_1_no_g), color_codes_where_K_0_not_equal_K_1_no_g])

    writer_not_connected.writerow([len(color_codes_where_K_0_not_equal_K_1_deterministic), color_codes_where_K_0_not_equal_K_1_deterministic])
    color_codes_where_K_0_not_equal_K_1_no_g_deterministic = [color_code for color_code in color_codes_where_K_0_not_equal_K_1_deterministic if 'g' not in color_code]
    writer_not_connected.writerow([len(color_codes_where_K_0_not_equal_K_1_no_g_deterministic), color_codes_where_K_0_not_equal_K_1_no_g_deterministic])

    for i in range(1, 5):
        G.add_edge(i, i+1)
    G.add_edge(5, 1)

    # for color_map_option in two_color_map_options:
    #     color_map = np.array(color_map_option).copy()
    #     color_map_option = list(np.array(color_map_option).copy())
    #     for i in range(len(color_map_option)):
    #         color_map_option[i] = 'red' if color_map_option[i] == 1 else ('blue' if color_map_option[i] == 2 else 'green')

    #     plt.clf()

    #     # Draw the graph
    #     nx.draw(G, pos=pos, with_labels=False, node_color=[color_map_option[node] for node in G.nodes()], node_size=1000)

    #     plt.annotate("You", xy=pos[0], xytext=(20, -10), textcoords='offset points', ha='left', va='center', fontsize=16, color='black', fontweight='bold')

    #     # Save the graph
    #     color_code = "".join([color[0] for color in color_map_option])
    #     plt.savefig("./human_experiment_visuals/two_connected/human_experiment_visual_%s.png" % color_code)
    #     simulate_deterministic_theory_of_mind(color_map, K=2)

    color_codes_where_K_0_not_equal_K_1 = []
    color_codes_where_K_0_not_equal_K_1_deterministic = []
    for color_map_option in three_color_map_options:
        color_map = np.array(color_map_option).copy()
        color_map_option = list(np.array(color_map_option).copy())
        for i in range(len(color_map_option)):
            color_map_option[i] = 'red' if color_map_option[i] == 1 else ('blue' if color_map_option[i] == 2 else 'green')
        color_code = "".join([color[0] for color in color_map_option])

        # plt.clf()
        # nx.draw(G, pos=pos, with_labels=False, node_color=[color_map_option[node] for node in G.nodes()], node_size=1000)
        # plt.annotate("You", xy=pos[0], xytext=(20, -10), textcoords='offset points', ha='left', va='center', fontsize=16, color='black', fontweight='bold')
        # plt.savefig("./human_experiment_visuals/three_not_connected/human_experiment_visual_%s.png" % color_code)
        
        K_0_not_equal_K_1, K_0_not_equal_K_1_deterministic = simulate_deterministic_theory_of_mind(3, color_map, color_code, K=1, csv_file_writer=writer_connected, iterations=1000)
        if K_0_not_equal_K_1:
            color_codes_where_K_0_not_equal_K_1.append(color_code)
        if K_0_not_equal_K_1_deterministic:
            color_codes_where_K_0_not_equal_K_1_deterministic.append(color_code)

    writer_connected.writerow([len(color_codes_where_K_0_not_equal_K_1), color_codes_where_K_0_not_equal_K_1])
    color_codes_where_K_0_not_equal_K_1_no_g = [color_code for color_code in color_codes_where_K_0_not_equal_K_1 if 'g' not in color_code]
    writer_connected.writerow([len(color_codes_where_K_0_not_equal_K_1_no_g), color_codes_where_K_0_not_equal_K_1_no_g])

    writer_connected.writerow([len(color_codes_where_K_0_not_equal_K_1_deterministic), color_codes_where_K_0_not_equal_K_1_deterministic])
    color_codes_where_K_0_not_equal_K_1_no_g_deterministic = [color_code for color_code in color_codes_where_K_0_not_equal_K_1_deterministic if 'g' not in color_code]
    writer_connected.writerow([len(color_codes_where_K_0_not_equal_K_1_no_g_deterministic), color_codes_where_K_0_not_equal_K_1_no_g_deterministic])
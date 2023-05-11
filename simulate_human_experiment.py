from itertools import product

import csv
import math
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

def simulate_deterministic_theory_of_mind(G, num_colors, color_map, color_code, K=0, csv_file_writer=None, iterations=1):
    # print(color_map, color_code)

    num_nodes = len(color_map)
    adjacency_matrix = nx.to_numpy_array(G, dtype=bool)

    num_color_choice_per_K = np.zeros((K+1, num_colors), dtype=int)
    csv_data = [color_code, "K=%d" % K, "iterations=%d" % iterations]
    stimuli_red = 1 if color_code[0] == 'r' else 0
    stimuli_blue = 1 if color_code[0] == 'b' else 0
    stimuli_green = 1 if color_code[0] == 'g' else 0
    stubborness_list = [iterations * stimuli_red, iterations * stimuli_blue, iterations * stimuli_green]
    for i in range(iterations):
        # print("iteration %d" % i)
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
    num_color_choice_per_K_inserted_stubborn = np.insert(num_color_choice_per_K, 0, stubborness_list, axis=0)
    csv_data.append(num_color_choice_per_K_inserted_stubborn.tolist())

    stubborn_equal_K_0 = np.all(num_color_choice_per_K_inserted_stubborn[0] == num_color_choice_per_K_inserted_stubborn[1])
    stubborn_equal_K_1 = np.all(num_color_choice_per_K_inserted_stubborn[0] == num_color_choice_per_K_inserted_stubborn[2])
    K_0_equal_K_1 = np.all(num_color_choice_per_K_inserted_stubborn[1] == num_color_choice_per_K_inserted_stubborn[2])

    csv_data.append(stubborn_equal_K_0)
    csv_data.append(stubborn_equal_K_1)
    csv_data.append(K_0_equal_K_1)

    shows_distinction = not stubborn_equal_K_0 or not stubborn_equal_K_1 or not K_0_equal_K_1
    csv_data.append(shows_distinction)

    if csv_file_writer is not None:
       csv_file_writer.writerow(csv_data) 

    return shows_distinction, stubborn_equal_K_0, stubborn_equal_K_1, K_0_equal_K_1

def remove_rotated_duplicates(list):
    unique_list = []
    for s in list:
        s_neighbor = s[1:]
        is_rotated_duplicate = False
        for i in range(len(s_neighbor)):
            rotated_s = s[0] + s_neighbor[i:] + s_neighbor[:i]  # rotate the string
            if rotated_s in unique_list:
                is_rotated_duplicate = True
                break
        if not is_rotated_duplicate:
            unique_list.append(s)
    return unique_list

if __name__ == '__main__':

    csv_file_connected = open("./human_experiment_simulation_data/three_connected.csv", "w")
    writer_connected = csv.writer(csv_file_connected)
    csv_file_not_connected = open("./human_experiment_simulation_data/three_not_connected.csv", "w")
    writer_not_connected = csv.writer(csv_file_not_connected)

    two_color_options = [1, 2, 3]
    two_color_map_options = list(product(two_color_options, repeat=6))

    # Create an empty graph
    G = nx.Graph()

    # Add six nodes to the graph
    G.add_nodes_from([0, 1, 2, 3, 4, 5,])

    # Add edges to connect one node to all other nodes
    for i in range(1, 6):
        G.add_edge(0, i)

    # Define the node positions
    c1 = math.cos(2*math.pi/5)
    c2 = math.cos(math.pi/5)
    s1 = math.sin(2*math.pi/5)
    s2 = math.sin(4*math.pi/5)
    pos = {0: (0, 0), 1: (0, 1), 2: (s1, c1), 3: (s2, -c2), 4: (-s2, -c2), 5: (-s1, c1)}

    not_connected_distinction = []
    for color_map_option in two_color_map_options:
        color_map = np.array(color_map_option).copy()
        color_map_option = list(np.array(color_map_option).copy())
        for i in range(len(color_map_option)):
            color_map_option[i] = 'red' if color_map_option[i] == 1 else ('blue' if color_map_option[i] == 2 else 'green')
        color_code = "".join([color[0] for color in color_map_option])
        shows_distinction, _, _, _ = simulate_deterministic_theory_of_mind(G, 3, color_map, color_code, K=1, csv_file_writer=writer_not_connected, iterations=1000)
        if shows_distinction:
            not_connected_distinction.append(color_code)
    writer_not_connected.writerow(np.insert(not_connected_distinction, 0, len(not_connected_distinction)))
    writer_not_connected.writerow(np.insert(remove_rotated_duplicates(not_connected_distinction), 0, len(remove_rotated_duplicates(not_connected_distinction))))

    for i in range(1, 5):
        G.add_edge(i, i+1)
    G.add_edge(5, 1)

    connected_distinction = []
    for color_map_option in two_color_map_options:
        color_map = np.array(color_map_option).copy()
        color_map_option = list(np.array(color_map_option).copy())
        for i in range(len(color_map_option)):
            color_map_option[i] = 'red' if color_map_option[i] == 1 else ('blue' if color_map_option[i] == 2 else 'green')
        color_code = "".join([color[0] for color in color_map_option])
        shows_distinction, _, _, _ = simulate_deterministic_theory_of_mind(G, 3, color_map, color_code, K=1, csv_file_writer=writer_connected, iterations=1000)
        if shows_distinction:
            connected_distinction.append(color_code)
    writer_connected.writerow(np.insert(connected_distinction, 0, len(connected_distinction)))
    writer_connected.writerow(np.insert(remove_rotated_duplicates(connected_distinction), 0, len(remove_rotated_duplicates(connected_distinction))))
# imports

from datetime import date

import argparse
import csv
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import random


# define run_trial()
def run_trial(args):

    # set up file names

    # create model name based on parameters 
    decision_making = "probability_matching" if args.probability_matching else "deterministic"
    model_name = "%s-memory_%d-stubbornness_%.2f_%.2f-randomness_%.2f_%.2f-unstuckness_%.2f_%.2f" % (decision_making, args.memory, args.stubbornness_low, args.stubbornness_high, args.randomness_low, args.randomness_high, args.unstuckness_low, args.unstuckness_high)

    # create trial setup name based on parameters
    trial_setup_name = "max_iterations_%d-cliques_%d-nodes_per_clique_%d-colors_%d-q_%d" % (args.max_iterations, args.cliques, args.nodes_per_clique, args.colors, args.q)

    # make directories if needed
    trial_path = args.model_location + model_name + "/" + trial_setup_name
    if not os.path.exists(trial_path):
        # os.makedirs(trial_path)
        os.makedirs(trial_path + "/animation/")
        os.makedirs(trial_path + "/csv/")
        os.makedirs(trial_path + "/component_plot/")

    # find trial index based on existing runs of this model (based on csv file existance)
    trial_index = 0
    csv_filename = args.model_location + model_name + "/" + trial_setup_name + "/csv/csv%d.csv" % trial_index
    while os.path.exists(trial_path + "/csv/csv%d.csv" % trial_index):
        trial_index += 1
        csv_filename = args.model_location + model_name + "/" + trial_setup_name + "/csv/csv%d.csv" % trial_index
    animation_filename = trial_path + "/animation/animation%d.gif" % trial_index
    component_plot_filename = args.model_location + model_name + "/" + trial_setup_name + "/component_plot/component_plot%d.png" % trial_index


    # set up csv writer
    csv_file = open(csv_filename, "w")
    writer = csv.writer(csv_file)


    # calculate remaining trial parameters

    num_nodes = args.cliques * args.nodes_per_clique
    stubbornness = list(np.random.uniform(low=args.stubbornness_low, high=args.stubbornness_high, size=num_nodes))
    randomness = list(np.random.uniform(low=args.randomness_low, high=args.randomness_high, size=num_nodes))
    unstuckness = list(np.random.uniform(low=args.unstuckness_low, high=args.unstuckness_high, size=num_nodes))

    # write randomized trial parameters to csv file
    writer.writerow(["stubbornness"])
    writer.writerow(stubbornness)
    writer.writerow(["randomness"])
    writer.writerow(randomness)
    writer.writerow(["unstuckness"])
    writer.writerow(unstuckness)


    # calculate the edges in clique 0 
    # clique 0 is the clique with nodes [0, args.nodes_per_clique])
    # this is used to make each clique into a clique and rewire

    edges_in_clique_0 = []
    for i in range(args.nodes_per_clique):
        for j in range(args.nodes_per_clique - i - 1):
            edges_in_clique_0.append((i+1, i+j+2))

    # set up the graph as G

    # create an array of each clique as an individual complete graph correctly numbered
    cliques = []
    for clique_i in range(args.cliques):
        G = nx.complete_graph(n=args.nodes_per_clique)
        G = nx.convert_node_labels_to_integers(G, first_label=1+args.nodes_per_clique*clique_i, ordering='default', label_attribute=None)
        cliques.append(G)

    # combine all cliques into a single graph G
    G = nx.compose_all(cliques)

    # create an array of connector edges that connect the cliques
    connector_edges = []
    for clique_i in range(args.cliques - 1):
        largest_node_in_lower_clique = (clique_i+1) * args.nodes_per_clique
        lowest_node_in_higher_clique = largest_node_in_lower_clique + 1
        connector_edges.append((largest_node_in_lower_clique, lowest_node_in_higher_clique))
    # combine the connector edges with all the cliques to create the default graph
    G.add_edges_from(connector_edges)

    # rewire the graph based on q
    for clique_i in range(args.cliques):
        for edge_i in edges_in_clique_0:
            rewire = random.random() < args.q
            if rewire:
                old_edge_a = args.nodes_per_clique*clique_i+edge_i[0]
                old_edge_b = args.nodes_per_clique*clique_i+edge_i[1]
                G.remove_edge(old_edge_a, old_edge_b)

                keep_a = random.random() < 0.5
                new_edge_a = old_edge_a if keep_a else old_edge_b
                new_edge_b = new_edge_a
                while(new_edge_a == new_edge_b or G.has_edge(new_edge_a, new_edge_b)):
                    new_edge_b = random.randint(1, num_nodes)
                G.add_edge(new_edge_a, new_edge_b)

    # confirm that the graph is connected
    # if the graph is not connected, close and delete the csv file, and exit
    if not nx.is_connected(G):
        print("G is not connected, ending and deleting trial...")
        csv_file.close()
        os.remove(csv_filename)
        exit()

    # get the adjacency matrix and write to csv
    adjacency_matrix = nx.to_numpy_array(G)
    writer.writerow(["adjacency matrix"])
    writer.writerow([adjacency_matrix.tolist()])

    # initialize node colors, node color history counts and total, node color history
    current_node_colors = list(np.random.randint(low = 0, high = args.colors, size = num_nodes))
    node_color_history_counts = np.zeros((num_nodes, args.colors), dtype=int)
    node_color_history_counts_total = []
    node_color_history = []

    # initialize biggest component color history and component proportion history
    biggest_component_color_history = []
    component_proportion_history = []


    # define update_color_history_counts()
    def update_color_history_counts(current_node_colors, node_color_history_counts):
        node_color_history_counts_total.append(node_color_history_counts.tolist())
        for i in range(num_nodes):
            node_i_curr_color_value = current_node_colors[i]
            node_color_history_counts[i][node_i_curr_color_value] += 1
        if len(node_color_history) > args.memory:
            for i in range(num_nodes):
                color_to_remove = node_color_history[-(args.memory+1)][i]
                node_color_history_counts[i][color_to_remove] -= 1

    # define update_color_history()
    def update_color_history(current_node_colors, node_color_history):
        color_history = []
        for index in range(num_nodes):
            color_history.append(current_node_colors[index])
        node_color_history.append(color_history)

    # define update_component_history()
    def update_component_history(current_node_colors, biggest_component_color_history, component_proportion_history):
        curr_node_colors_bincount = np.bincount(current_node_colors, minlength=args.colors)
        biggest_component_color_history.append(np.argmax(curr_node_colors_bincount))
        component_proportion_history.append([(x/num_nodes) for x in curr_node_colors_bincount])


    # update color history counts, color history, component history with initialization
    update_color_history_counts(current_node_colors, node_color_history_counts)
    update_color_history(current_node_colors, node_color_history)
    update_component_history(current_node_colors, biggest_component_color_history, component_proportion_history)


    # define run_consensus_iteration():
    def run_consensus_iteration(iteration):
        # if the entire trial was initialized to the same color, return that it took zero iterations and completion
        if iteration == 0 and current_node_colors.count(current_node_colors[0]) == len(current_node_colors):
            return 0, current_node_colors.count(current_node_colors[0]) == len(current_node_colors)

        # every node goes through the color decision each iteration
        for i in range(num_nodes):

            # if node is randomly stubborn, stay the same color
            is_stubborn = random.random() < stubbornness[i]
            if is_stubborn:
                continue

            # if node is randomly random, select a random color
            is_random = random.random() < randomness[i]
            if is_random:
                current_node_colors[i] = np.random.randint(low=0, high=trial_num_colors)
                continue

            # remove all values that are not neighbors
            neighbor_node_color_history = node_color_history_counts * adjacency_matrix[i].reshape((num_nodes, 1))
            # add one to every value to avoid multiplying by zero
            neighbor_node_color_history_no_zeroes = np.asarray([x+1 for x in neighbor_node_color_history])
            # calculate the probability that each neighbor selects a given color
            neighbor_node_color_probability = neighbor_node_color_history_no_zeroes/(args.colors+iteration+1)
            # calculate the probability that all neighbors select a given color
            neighbor_column_node_color_probability = np.prod(neighbor_node_color_probability, axis=0)

            # if node is randomly unstuck, ignore the highest probability options
            is_unstuck = random.random() < unstuckness[i]
            if is_unstuck:
                columns_with_highest_probability = np.argwhere(neighbor_column_node_color_probability == np.amax(neighbor_column_node_color_probability))
                for column_with_highest_probability in columns_with_highest_probability:
                    neighbor_column_node_color_probability[column_with_highest_probability] = 0
                # go through normal decision making after removing the highest probability option from consideration

            # normal decision making (e.g., no stubborn, random, unstuck individual behaviors)
            # if decision making with probability matching
            if args.probability_matching:
                # normalize the probability that all neighbors select a given color
                neighbor_column_node_color_probability_normalized = neighbor_column_node_color_probability/sum(neighbor_column_node_color_probability)
                # randomly select a color using the normalized probabilities
                current_node_colors[i] = np.random.choice(np.arange(num_colors), p=neighbor_column_node_color_probability_normalized)
            # if decision making with deterministic selection
            else:
                # find the nodes with the highest probability that all neighbors select a given color
                columns_with_highest_probability = np.argwhere(neighbor_column_node_color_probability == np.amax(neighbor_column_node_color_probability))
                # randomly select one node from those with the highest probability
                current_node_colors[i] = random.choice(columns_with_highest_probability)[0]

        # update color history counts, color history, component history with each iteration
        update_color_history_counts(current_node_colors, node_color_history_counts)
        update_color_history(current_node_colors, node_color_history)
        update_component_history(current_node_colors, biggest_component_color_history, component_proportion_history)

        # return next iteration (number of iterations run so far), and completion
        return iteration+1, current_node_colors.count(current_node_colors[0]) == len(current_node_colors) 


    # run all iterations in trial until max iterations hit or consensus successfully reached
    iteration = 0
    done = False
    while iteration < args.max_iterations and not done: 
            iteration, done = run_consensus_iteration(iteration)


    # write node color history, node color history counts, and component proportion history to csv
    writer.writerow(["node color history"])
    writer.writerow([node_color_history])
    writer.writerow(["node color history counts total"])
    writer.writerow([node_color_history_counts_total])
    writer.writerow(["biggest component color history"])
    writer.writerow(biggest_component_color_history)
    writer.writerow(["component proportion history"])
    writer.writerow([component_proportion_history])


    # close csv file
    csv_file.close()
    print("Trial data saved to %s", csv_filename)


    # if specified, animate
    if args.animation:

        # define init_func()
        def init_func():
            return nodes,

        # define animate()
        def animate(frame):
            ax = plt.gca()
            ax.set_title("Time " + str(frame))
            nc = node_color_history[frame]
            nodes.set_array(nc)
            return nodes,

        # layout and draw graph
        pos = nx.spring_layout(G)
        nodes = nx.draw_networkx_nodes(G, pos, cmap=plt.cm.tab10, node_color=range(num_nodes), vmin=0, vmax=args.colors)
        edges = nx.draw_networkx_edges(G, pos)
        edges = nx.draw_networkx_labels(G, pos)
        plt.axis('off')

        # run animation
        fig = plt.gcf()
        ani = animation.FuncAnimation(fig, animate, init_func=init_func, interval=500, frames=iteration+1, blit=True)

        # save animation
        ani.save(animation_filename)
        print("Trial animation saved to %s", animation_filename)

    # if specified, plot the component proportions
    if args.component_plot:
        plt.clf()
        plt.title("Color Proportions over Trial")

        component_proportion_history = np.array(component_proportion_history)
        for i in range(args.colors):
            plt.plot(component_proportion_history[:,i])

        plt.savefig(component_plot_filename)
        print("Trial component plot saved to %s", component_plot_filename)


if __name__ == '__main__':

    # parse arguments into trial parameters

    parser = argparse.ArgumentParser()

    # file parameters
    parser.add_argument("--model_location", type=str, default="./data/individual_models/")
    parser.add_argument("--animation", action=argparse.BooleanOptionalAction)
    parser.add_argument("--component_plot", action=argparse.BooleanOptionalAction)
    # note, csv files are always recorded

    # model parameters
    parser.add_argument("--probability_matching", action=argparse.BooleanOptionalAction)
    parser.add_argument("--memory", type=int, default=0)
    parser.add_argument("--stubbornness_low", type=float, default=0.0)
    parser.add_argument("--stubbornness_high", type=float, default=0.0)
    parser.add_argument("--randomness_low", type=float, default=0.0)
    parser.add_argument("--randomness_high", type=float, default=0.0)
    parser.add_argument("--unstuckness_low", type=float, default=0.0)
    parser.add_argument("--unstuckness_high", type=float, default=0.0)

    # trial setup parameters
    parser.add_argument("--max_iterations", type=int, default=180)
    parser.add_argument("--cliques", type=int, default=6)
    parser.add_argument("--nodes_per_clique", type=int, default=6)
    parser.add_argument("--colors", type=int, default=9)
    parser.add_argument("--q", type=float, default=0)

    args = parser.parse_args()

    run_trial(args)
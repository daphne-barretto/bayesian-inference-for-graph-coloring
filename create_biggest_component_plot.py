import argparse
import csv
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str, required=True)
parser.add_argument("--save_location", type=str, required=True)
args = vars(parser.parse_args())

with open(args["filename"], newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    rows = list(reader)
    
    max_iterations = int(rows[1][2])
    biggest_component_color_history = [int(x) for x in rows[7]]
    biggest_component_proportion_history = rows[8]

    plt.title(args["save_location"] + ", " + biggest_component_proportion_history[-1])
    plt.scatter(np.arange(len(biggest_component_proportion_history)), biggest_component_proportion_history, c=biggest_component_color_history, s=6)
    # plt.gca().set_ylim(bottom=0)
    # plt.plot(biggest_component_proportion_history)
    # plt.xlim([0, max_iterations])
    # plt.ylim(-1, 1.0)
    # ax = plt.gca()
    # ax.set_
    # yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    # ax.set_yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    # ax.set_ylim([0, 1])
    # ax.set_yticks((0.0, 1.0))
    # plt.show()
    plt.savefig(args["save_location"])
    
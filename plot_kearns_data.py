# imports

import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

if __name__ == '__main__':

    q_options = [0, 0.1, 0.2, 0.4, 0.6, 1]

    human_behavior_consensus = [156.43, 63.57, 50.00, 30.71, 27.85, 18.57]
    heuristic_model_consensus = [180.00, 180.00, 177.14, 136.43, 70.71, 67.14]

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

    plt.clf()
    fig = plt.figure()
    ax = fig.gca()

    # my_cmap = plt.cm.hsv(np.arange(plt.cm.RdBu.N))
    # my_cmap[:,0:3] *= 0.8
    # my_cmap = ListedColormap(my_cmap)

    # plt.gca().set_prop_cycle(plt.cycler('color', my_cmap(np.linspace(0, 1, 2))))

    plt.title("Human Behavior and Heuristic Model: Average Running Time per q")
    plt.xlabel("rewiring probability, q")
    plt.ylabel("running time (seconds)")

    ax.tick_params(axis="x", direction="in")
    ax.tick_params(axis="y", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(0.05))
    ax.tick_params(axis="x", which='minor', direction="in")

    plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0])
    plt.xlim([-0.02, 1.02])
    plt.yticks([0, 30, 60, 90, 120, 150, 180], [0, 30, 60, 90, 120, 150, 180])
    plt.ylim([0, 185])

    plt.plot(q_options, human_behavior_consensus, "o-", label=("human behavior"))
    plt.plot(q_options, heuristic_model_consensus, "o--", label=(("heuristic model")))

    plt.legend()

    plt.savefig("./data/kearns_extracted_data/kearns_avg_running_time_per_q.png")
    plt.close() 
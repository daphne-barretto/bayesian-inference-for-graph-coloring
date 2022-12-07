# For every set of model parameters (not q or graph parameters),
# create a line for the line chart
# and plot running time (iterations) over q

# note there are 8 * 2 iterations of the model with 6 q values each

import csv
import matplotlib.pyplot as plt
import numpy as np
import os

colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

iterations = 5 * 2
probability_matching_options = [True, False]
memory_options = [0, 1, 2, 3, 100]

q_options = [0, 0.1, 0.2, 0.4, 0.6, 1]

avg_solution_times = []

for i in range(iterations):
    '''
        T/F
        memory [0, 1, 2, 3, 100]
    '''

    probability_matching_selection = False
    if i < 5:
        probability_matching_selection = probability_matching_options[0]
    else:
        probability_matching_selection = probability_matching_options[1]

    memory_selection = memory_options[i % 5]

    found_all = False
    found_count = [0, 0, 0, 0, 0, 0]
    found_iteration_totals = [0, 0, 0, 0, 0, 0]
    q_iteration = 0
    while not found_all:
        q_selection = q_options[q_iteration]
        found_count_selection = found_count[q_iteration]
        filename = ("./data/csv/csv_2022-11-20_dict_values([True- %s- %d- 60- 6- 6- 9- 0.0- 0.0- %.1f])_%d.csv" % (probability_matching_selection, memory_selection, q_selection, found_count_selection))
        # print("Looking for file: ", filename)
        if os.path.exists(filename):
            print("Getting file named: ", filename)
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                rows = list(reader)

                if len(rows) < 11 or len(rows[10]) < 2:
                    continue

                iteration_value = rows[10][1]
                print("Trial took %s iterations" % iteration_value)

                found_count[q_iteration] += 1
                found_iteration_totals[q_iteration] += int(iteration_value)
        elif q_iteration + 1 < len(q_options):
            q_iteration += 1
        else:
            found_all = True

    avg_solution_time = np.divide(found_iteration_totals, found_count)
    avg_solution_times.append(avg_solution_time)

    plt.clf()
    plt.title("Prob. Match: %s, Memory: %d" % (probability_matching_selection, memory_selection))
    plt.xlabel("rewiring probability, q")
    plt.ylabel("running time (iterations), max 60")
    plt.xlim([0.0, 1.1])
    plt.ylim([0, 61])
    plt.plot(q_options, avg_solution_time, label=("%s%d")%(probability_matching_selection, memory_selection), c=colors[i])
    plt.legend()
    plt.savefig("./data/comparison_plots/comparison-%s-%d.png" % (probability_matching_selection, memory_selection))

plt.clf()
plt.title("Prob. Match: %s, Memory: %d" % (probability_matching_selection, memory_selection))
plt.xlabel("rewiring probability, q")
plt.ylabel("running time (iterations), max 60")
plt.xlim([0.0, 1.1])
plt.ylim([0, 61])
for i in range(iterations):
    probability_matching_selection = False
    if i < 5:
        probability_matching_selection = probability_matching_options[0]
    else:
        probability_matching_selection = probability_matching_options[1]

    memory_selection = memory_options[i % 5]

    plt.plot(q_options, avg_solution_times[i], label=("%s%s"%(probability_matching_selection, memory_selection)))
plt.legend()
plt.savefig("./data/comparison_plots/comparison-all.png")

print(q_options)
print(avg_solution_times)
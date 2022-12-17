# imports

from itertools import product

import csv
import numpy as np


if __name__ == '__main__':

    human_behavior_consensus = [156.43, 63.57, 50.00, 30.71, 27.85, 18.57]
    heuristic_model_consensus = [180.00, 180.00, 177.14, 136.43, 70.71, 67.14]

    print("correlation between human behavior and heuristic model: %.2f" % np.corrcoef([human_behavior_consensus, heuristic_model_consensus])[1][0])
    print("correlation between human behavior and heuristic model: %.2f" % np.corrcoef([human_behavior_consensus[2:], heuristic_model_consensus[2:]])[1][0])
    print("correlation between human behavior and heuristic model: %.2f" % np.corrcoef([human_behavior_consensus[3:], heuristic_model_consensus[3:]])[1][0])

    csv_file_read = open("./data/model_comparisons/analysis_avg_solution_time_heterogeneous.csv", "r")

    reader = csv.reader(csv_file_read, delimiter=',')
    rows = list(reader)

    csv_file_write = open("./data/model_comparisons/correlations_heterogeneous.csv", "w")
    writer = csv.writer(csv_file_write)

    all_model_avg_solution_time = rows[5]

    heterogeneity_options = ["randomness", "stubbornness", "unstuckness"]
    heterogeneity_high_options = np.linspace(0.1,1.0,10)
    heterogeneity_model_options = list(product(heterogeneity_options, heterogeneity_high_options))

    probability_matching_options = ["probability_matching", "deterministic"]
    memory_options = list(range(0, 11))
    model_options = list(product(probability_matching_options, memory_options))

    i = 0
    for heterogeneity_model_option in heterogeneity_model_options:
        for probability_matching_option in probability_matching_options:

            for memory_option in memory_options:

                model_avg_solution_time = list(map(float, all_model_avg_solution_time[i][1:-1].split(", ")))
                print(model_avg_solution_time)
                delta = 0.001
                if len(set(model_avg_solution_time)) <= 1: # if the model avg solution time is all equal
                    model_avg_solution_time[-1] = model_avg_solution_time[0] + delta

                correlation_between_human_behavior_and_model_all = np.corrcoef([human_behavior_consensus, model_avg_solution_time])[1][0],
                correlation_between_human_behavior_and_model_starting_q_01 = np.corrcoef([human_behavior_consensus[1:], model_avg_solution_time[1:]])[1][0]
                correlation_between_human_behavior_and_model_starting_q_02 = np.corrcoef([human_behavior_consensus[2:], model_avg_solution_time[2:]])[1][0]
                correlation_between_human_behavior_and_model_starting_q_04 = np.corrcoef([human_behavior_consensus[3:], model_avg_solution_time[3:]])[1][0]

                correlation_between_heuristic_model_and_model_all = np.corrcoef([heuristic_model_consensus, model_avg_solution_time])[1][0],
                correlation_between_heuristic_model_and_model_starting_q_01 = np.corrcoef([heuristic_model_consensus[1:], model_avg_solution_time[1:]])[1][0]
                correlation_between_heuristic_model_and_model_starting_q_02 = np.corrcoef([heuristic_model_consensus[2:], model_avg_solution_time[2:]])[1][0]
                correlation_between_heuristic_model_and_model_starting_q_04 = np.corrcoef([heuristic_model_consensus[3:], model_avg_solution_time[3:]])[1][0]

                writer.writerow([
                    heterogeneity_model_option[0], 
                    heterogeneity_model_option[1],
                    probability_matching_option,
                    memory_option,
                    correlation_between_human_behavior_and_model_all[0],
                    correlation_between_human_behavior_and_model_starting_q_01,
                    correlation_between_human_behavior_and_model_starting_q_02,
                    correlation_between_human_behavior_and_model_starting_q_04,
                    correlation_between_heuristic_model_and_model_all[0],
                    correlation_between_heuristic_model_and_model_starting_q_01,
                    correlation_between_heuristic_model_and_model_starting_q_02,
                    correlation_between_heuristic_model_and_model_starting_q_04
                ])

                i += 1

    csv_file_read.close()
    csv_file_write.close()
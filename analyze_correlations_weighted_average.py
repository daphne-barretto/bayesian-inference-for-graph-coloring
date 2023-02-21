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

    csv_file_read = open("./data/model_comparisons/analysis_avg_solution_time_weighted_average_180_pm.csv", "r")

    reader = csv.reader(csv_file_read, delimiter=',')
    rows = list(reader)

    csv_file_write = open("./data/model_comparisons/correlations_weighted_average_180_pm.csv", "w")
    writer = csv.writer(csv_file_write)

    all_model_avg_solution_time = rows[5]

    decision_making_calculation_options = ["sum"]
    probability_matching_options = ["probability_matching"]
    memory_options = list(range(0, 181))
    model_options = list(product(decision_making_calculation_options, probability_matching_options, memory_options))

    i = 0
    for model_option in model_options:
        model_avg_solution_time = list(map(float, all_model_avg_solution_time[i][1:-1].split(", ")))
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
            model_option[1], 
            model_option[2],
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

    # index = 1
    # model_option = model_options[index]
    # model_avg_solution_time = list(map(float, all_model_avg_solution_time[index][1:-1].split(", ")))

    # delta = 0.001
    # if len(set(model_avg_solution_time)) <= 1: # if the model avg solution time is all equal
    #     model_avg_solution_time[-1] = model_avg_solution_time[0] + delta

    # print(model_avg_solution_time)

    # print(model_option, np.corrcoef([human_behavior_consensus, model_avg_solution_time])[1][0])
    # print(model_option, np.corrcoef([human_behavior_consensus[2:], model_avg_solution_time[2:]])[1][0])
    # print(model_option, np.corrcoef([human_behavior_consensus[3:], model_avg_solution_time[3:]])[1][0])

    # print(model_option, np.corrcoef([heuristic_model_consensus, model_avg_solution_time])[1][0])
    # print(model_option, np.corrcoef([heuristic_model_consensus[2:], model_avg_solution_time[2:]])[1][0])
    # print(model_option, np.corrcoef([heuristic_model_consensus[3:], model_avg_solution_time[3:]])[1][0])
    
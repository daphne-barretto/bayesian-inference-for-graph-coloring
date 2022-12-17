# imports

from itertools import product

import ast
import csv
import numpy as np
import os
import sys


if __name__ == '__main__':

    csv.field_size_limit(sys.maxsize)

    q_list = [0, 0.1, 0.2, 0.4, 0.6, 1.0]

    heterogeneity_options = ["randomness", "stubbornness", "unstuckness"]
    heterogeneity_high_options = np.linspace(0.1,1.0,10)
    heterogeneity_model_options = list(product(heterogeneity_options, heterogeneity_high_options))

    probability_matching_options = ["probability_matching", "deterministic"]
    memory_options = list(range(0, 11))
    model_options = list(product(probability_matching_options, memory_options))

    all_model_trial_counts = []
    all_model_iteration_totals = []
    all_model_avg_solution_time = []
    all_model_success_rates = []

    for heterogeneity_model_option in heterogeneity_model_options:
        model_location = "./data/individual_models_with_%s_0.00_%.2f" % (heterogeneity_model_option[0], heterogeneity_model_option[1])

        model_location_files = os.listdir(model_location)
        assert len(model_location_files) >= 11, "%d models found, not at least 11: %s" % (len(model_location_files), model_location)

        for model_option in model_options:
            stubbornness_high = heterogeneity_model_option[1] if heterogeneity_model_option[0] == "stubbornness" else 0.00
            randomness_high = heterogeneity_model_option[1] if heterogeneity_model_option[0] == "randomness" else 0.00
            unstuckness_high = heterogeneity_model_option[1] if heterogeneity_model_option[0] == "unstuckness" else 0.00

            model_option_location = model_location + "/%s-memory_%d-stubbornness_0.00_%.2f-randomness_0.00_%.2f-unstuckness_0.00_%.2f" % (model_option[0], model_option[1], stubbornness_high, randomness_high, unstuckness_high)
            trial_setup_location_files = os.listdir(model_option_location)
            assert len(trial_setup_location_files) == 6, "Only %d trial setups found, not 6: %s" % (len(trial_setup_location_files), model_option_location)

            q_index = 0

            model_trial_counts = [0] * len(q_list)
            model_iteration_totals = [0] * len(q_list)

            model_success_counts = [0] * len(q_list)

            for q in q_list:
                trial_location = model_option_location + "/max_iterations_180-cliques_6-nodes_per_clique_6-colors_9-q_%.2f" % q
                trial_location_files = os.listdir(trial_location)
                assert len(trial_location_files) == 3, "Only %d trial folders found, not 3: %s" % (len(trial_location_files), trial_location)

                for i in range(30):
                    if not os.path.exists(trial_location + "/csv/csv%d.csv" % i):
                        print("You are missing trials")
                        # os.system("python run_trial.py %s --memory %d --q %.2f --animation --component_plot" % ("--probability_matching" if model_option[0] == "probability_matching" else "", model_option[1], q))
                    elif not os.path.exists(trial_location + "/animation/animation%d.gif" % i) or not  os.path.exists(trial_location + "/component_plot/component_plot%d.png" % i):
                        os.remove(trial_location + "/csv/csv%d.csv" % i)
                        print("You are missing trials, there was corrupted data")
                        os.system("python run_set_of_trials_for_model_across_q.py --animation --component_plot --trials 30 --memory %d" % model_option[1])

                # i = 100
                # while len(os.listdir(trial_location + "/csv/")) > 100 or len(os.listdir(trial_location + "/animation/")) > 100 or len(os.listdir(trial_location + "/component_plot/")) > 100:
                #     if os.path.exists(trial_location + "/csv/csv%d.csv" % i):
                #         os.remove(trial_location + "/csv/csv%d.csv" % i)
                #     if os.path.exists(trial_location + "/animation/animation%d.gif" % i):
                #         os.remove(trial_location + "/animation/animation%d.gif" % i)
                #     if os.path.exists(trial_location + "/component_plot/component_plot%d.png" % i):
                #         os.remove(trial_location + "/component_plot/component_plot%d.png" % i)
                #     i += 1

                assert len(os.listdir(trial_location + "/csv/")) >= 30, "%d csv files found, not 30: %s" % (len(os.listdir(trial_location + "/csv/")), trial_location)
                assert len(os.listdir(trial_location + "/animation/")) >= 30, "%d gif files found, not 30: %s" % (len(os.listdir(trial_location + "/animation/")), trial_location)
                assert len(os.listdir(trial_location + "/component_plot/")) >= 30, "%d png files found, not 30: %s" % (len(os.listdir(trial_location + "/component_plot/")), trial_location)

                for i in range(30):
                    csv_file_location = trial_location + "/csv/csv%d.csv" % i
                    assert os.path.exists(csv_file_location), "csv%d.csv not found in %s" % (i, trial_location_files)
                    
                    assert os.path.exists(trial_location + "/animation/animation%d.gif" % i), "animation%d.gif not found in %s" % (i, trial_location_files)
                    assert os.path.exists(trial_location + "/component_plot/component_plot%d.png" % i), "component_plot%d.png not found in %s" % (i, trial_location_files)

                    with open(csv_file_location, newline='') as csvfile:
                        # print("Reading ", csv_file_location)
                        reader = csv.reader(csvfile, delimiter=',')
                        rows = list(reader)
                        assert(len(rows) == 16)
                        assert(rows[0][0] == "stubbornness")
                        assert(rows[2][0] == "randomness")
                        assert(rows[4][0] == "unstuckness")
                        assert(rows[6][0] == "adjacency matrix")
                        assert(rows[8][0] == "node color history")
                        assert(rows[10][0] == "node color history counts total")
                        assert(rows[12][0] == "biggest component color history")
                        assert(rows[14][0] == "component proportion history")

                        model_trial_counts[q_index] += 1
                        model_iteration_totals[q_index] += len(rows[13]) - 1

                        last_component_proportion = rows[15][0]
                        last_component_proportion = ast.literal_eval(last_component_proportion)[-1]
                        count_ones = 0
                        definitely_not_consensus = False
                        for proportion in last_component_proportion:
                            if proportion == 1:
                                count_ones += 1
                            elif proportion != 0:
                                definitely_not_consensus = True
                                break
                        if count_ones == 1 and not definitely_not_consensus:
                            model_success_counts[q_index] += 1

                q_index += 1

            model_avg_solution_time = np.divide(model_iteration_totals, model_trial_counts)
            model_success_rate = np.divide(model_success_counts,model_trial_counts)

            all_model_trial_counts.append(model_trial_counts)
            all_model_iteration_totals.append(model_iteration_totals)
            all_model_avg_solution_time.append(model_avg_solution_time.tolist())
            all_model_success_rates.append(model_success_rate)
            print(model_success_rate)

    csv_file = open("./data/model_comparisons/analysis_avg_solution_time_heterogeneous.csv", "w")
    writer = csv.writer(csv_file)
    writer.writerow(["all_model_trial_counts"])
    writer.writerow(all_model_trial_counts)
    writer.writerow(["all_model_iteration_totals"])
    writer.writerow(all_model_iteration_totals)
    writer.writerow(["all_model_avg_solution_time"])
    writer.writerow(all_model_avg_solution_time)
    writer.writerow(["all_model_success_rate"])
    writer.writerow(all_model_success_rates)
    csv_file.close()
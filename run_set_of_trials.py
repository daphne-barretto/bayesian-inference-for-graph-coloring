from datetime import date

import os

    # is_consensus_not_unique_coloring = True
    # is_consensus_probability_matching = True
    # max_iterations = 500

    # trial_num_cliques = 6
    # trial_num_nodes_per_clique = 6
    # trial_num_colors = 10
    # trial_stubborness_quotient_low = 0.0
    # trial_stubborness_quotient_high = 1.0
    # q = 0.9

today = date.today().isoformat()
file_index = 0
while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
    file_index += 1
output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"
biggest_component_plot_filename = './data/biggest_component_plot/biggest_component_plot_' + today + "_" + str(file_index) + ".png"

for i in range(50):
    os.system("touch " + output_filename)
    os.system("python run_trial.py > " + output_filename)
    # os.system("python create_biggest_component_plot.py --filename " + csv_filename + " --save_location " + biggest_component_plot_filename)
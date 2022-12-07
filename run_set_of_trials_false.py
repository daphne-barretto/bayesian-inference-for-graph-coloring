from datetime import date

import os

def run_trial_true(memory, trials):
    q_list = [0.0, 0.1, 0.2, 0.4, 0.6, 1.0]

    for i in range(trials):
        for q in q_list:

            today = date.today().isoformat()
            file_index = 0
            while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
                file_index += 1
            output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"

            os.system("python run_trial_true.py "
                + "--is_consensus_not_unique_coloring True " 
                + "--memory %d " % memory
                + "--max_iterations 60 " 
                + "--trial_num_cliques 6 " 
                + "--trial_num_nodes_per_clique 6 " 
                + "--trial_num_colors 9 " 
                + "--trial_stubborness_quotient_low 0.0 " 
                + "--trial_stubborness_quotient_high 0.0 " 
                + "--q %f " % q
                + "> " + output_filename
                )

memory_list = [4, 5, 10, 20, 30, 40, 50, 60]
for memory in memory_list:
    run_trial_true(memory, 50)
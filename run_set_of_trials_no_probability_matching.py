from datetime import date

import os

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 0 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 0 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 0 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.2 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 0 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.4 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 0 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.6 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 0 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 1 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 1 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 1 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.2 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 1 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.4 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 1 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.6 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 1 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.2 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.4 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.6 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.2 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.4 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.6 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.2 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.4 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.6 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 2 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 1 " 
        + "> " + output_filename
        )

# memory 3

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 3 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 3 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 3 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.2 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 3 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.4 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 3 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.6 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 3 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 1 " 
        + "> " + output_filename
        )

# memory max

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.2 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.4 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.6 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.1 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.2 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.4 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 0.6 " 
        + "> " + output_filename
        )

for i in range(50):

    today = date.today().isoformat()
    file_index = 0
    while os.path.exists("./data/animations/animation_" + today + "_%s.gif" % file_index):
        file_index += 1
    output_filename = './data/output/output_' + today + "_" + str(file_index) + ".txt"
    csv_filename = './data/csv/csv_' + today + "_" + str(file_index) + ".csv"

    os.system("python run_trial.py "
        + "--is_consensus_not_unique_coloring True " 

        + "--memory 100 " 
        + "--max_iterations 60 " 
        + "--trial_num_cliques 6 " 
        + "--trial_num_nodes_per_clique 6 " 
        + "--trial_num_colors 9 " 
        + "--trial_stubborness_quotient_low 0.0 " 
        + "--trial_stubborness_quotient_high 0.0 " 
        + "--q 1 " 
        + "> " + output_filename
        )
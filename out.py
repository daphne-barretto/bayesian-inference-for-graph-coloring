files = []

for memory in range(181):
    model_folder = "data/individual_models/deterministic-memory_%i-stubbornness_0.00_0.00-randomness_0.00_0.00-unstuckness_0.00_0.00/" % memory

    for q in [0.00, 0.10, 0.20, 0.40, 0.60, 1.00]:
        trial_setup_folder = model_folder + "max_iterations_180-cliques_6-nodes_per_clique_6-colors_9-q_%.2f/" % q

        for trial in range(100):
            current_filepath = trial_setup_folder + "csv/csv%i.csv" % trial
            files.append(current_filepath)

for memory in range(181):
    model_folder = "data/individual_models/probability_matching-memory_%i-stubbornness_0.00_0.00-randomness_0.00_0.00-unstuckness_0.00_0.00/" % memory

    for q in [0.00, 0.10, 0.20, 0.40, 0.60, 1.00]:
        trial_setup_folder = model_folder + "max_iterations_180-cliques_6-nodes_per_clique_6-colors_9-q_%.2f/" % q

        for trial in range(100):
            current_filepath = trial_setup_folder + "csv/csv%i.csv" % trial
            files.append(current_filepath)

for heterogeneity_index, heterogeneity in enumerate(["stubbornness", "randomness", "unstuckness"]):
    for heterogeneity_high in [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]:
        for decision_making_type in ["deterministic", "probability_matching"]:
            for memory in range(11):
                for q in [0.00, 0.10, 0.20, 0.40, 0.60, 1.00]:
                    for trial in range(30):
                        outer_model_folder = "data/individual_models_with_%s_0.00_%.2f/" % (heterogeneity, heterogeneity_high)
                        heterogeneity_highs = [0.00, 0.00, 0.00]
                        heterogeneity_highs[heterogeneity_index] = heterogeneity_high
                        model_folder = outer_model_folder + "%s-memory_%i-stubbornness_0.00_%.2f-randomness_0.00_%.2f-unstuckness_0.00_%.2f/" % (decision_making_type, memory, heterogeneity_highs[0], heterogeneity_highs[1], heterogeneity_highs[2])
                        trial_setup_folder = model_folder + "max_iterations_180-cliques_6-nodes_per_clique_6-colors_9-q_%.2f/" % q
                        current_filepath = trial_setup_folder + "csv/csv%i.csv" % trial
                        files.append(current_filepath)

with open('./csvfiles.txt', 'w') as fp:
    fp.write("\n".join(str(item) for item in files))
# imports

from argparse import Namespace
from itertools import product
from run_trial import run_trial


# define run_set_of_trials_across_q
def run_set_of_trials_across_q(args, trials):
    q_list = [0.0, 0.1, 0.2, 0.4, 0.6, 1.0]

    for i in range(trials):
        for q in q_list:
            args.q = q
            run_trial(args)


if __name__ == '__main__':

    probability_matching_options = [True, False]
    memory_options = list(range(0, 181))
    # stubbornness_low_options = [x * 0.1 for x in range(0, 11)]
    # stubbornness_high_options = [x * 0.1 for x in range(0, 11)]
    # randomness_low_options = [x * 0.1 for x in range(0, 11)]
    # randomness_high_options = [x * 0.1 for x in range(0, 11)]
    # unstuckness_low_options = [x * 0.1 for x in range(0, 11)]
    # unstuckness_high_options = [x * 0.1 for x in range(0, 11)]

    args_options = list(product(probability_matching_options, memory_options))
    # print(args_options)

    for i in range(len(args_options)):

        # set up arguments, particularly model arguments
        args = Namespace(
            model_location = "./data/individual_models/",
            animation = True,
            component_plot = True,

            probability_matching = args_options[i][0],
            memory = args_options[i][1],
            stubbornness_low = 0.0,
            stubbornness_high = 0.0,
            randomness_low = 0.0,
            randomness_high = 0.0,
            unstuckness_low = 0.0,
            unstuckness_high = 0.0,

            max_iterations = 180,
            cliques = 6,
            nodes_per_clique = 6,
            colors = 9,
            q = 0.0
        )

        run_set_of_trials_across_q(args, 100)
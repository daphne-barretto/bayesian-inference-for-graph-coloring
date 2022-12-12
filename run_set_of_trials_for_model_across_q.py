# imports

from argparse import Namespace
from itertools import product
from run_trial import run_trial

import argparse

# define run_set_of_trials_across_q
def run_set_of_trials_across_q(args, trials):
    q_list = [0.0, 0.1, 0.2, 0.4, 0.6, 1.0]

    for i in range(trials):
        for q in q_list:
            args.q = q
            run_trial(args)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--probability_matching", action=argparse.BooleanOptionalAction)
    parser.add_argument("--memory", type=int, default=0)
    parser.add_argument("--trials", type=int, default=100)
    args = parser.parse_args()

    args = Namespace(
            model_location = "./data/individual_models/",
            animation = True,
            component_plot = True,

            probability_matching = args.probability_matching,
            memory = args.memory,
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

    run_set_of_trials_across_q(args, args.trials)
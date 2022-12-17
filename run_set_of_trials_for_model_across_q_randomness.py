# imports

from argparse import Namespace
from itertools import product
from run_trial import run_trial

import argparse
import os

# define run_set_of_trials_across_q
def run_set_of_trials_across_q(args, trials=0):
    q_list = [0.0, 0.1, 0.2, 0.4, 0.6, 1.0]
    unstuckness_high_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    for q in q_list:
        args.q = q

        # if not q == 0.0:
        #     args.memory = args.memory - 90

        for unstuckness_high in unstuckness_high_list:
            args.randomness_high = unstuckness_high
            # model_location = args.model_location
            model_location = "./data/individual_models_with_randomness_0.00_%.2f" % unstuckness_high
            args.model_location = "./data/individual_models_with_randomness_0.00_%.2f" % unstuckness_high
            model_option_location = model_location + "/%s-memory_%d-stubbornness_0.00_0.00-randomness_0.00_%.2f-unstuckness_0.00_0.00" % ("probability_matching", args.memory, unstuckness_high)
            trial_location = model_option_location + "/max_iterations_180-cliques_6-nodes_per_clique_6-colors_9-q_%.2f" % q
            if not os.path.exists(trial_location):
                os.makedirs(trial_location + "/animation/")
                os.makedirs(trial_location + "/csv/")
                os.makedirs(trial_location + "/component_plot/")
            print(len(os.listdir(trial_location + "/csv/")))
            while len(os.listdir(trial_location + "/csv/")) < trials:
                args.probability_matching = True
                run_trial(args)

        for unstuckness_high in unstuckness_high_list:
            args.randomness_high = unstuckness_high
            # model_location = args.model_location
            model_location = "./data/individual_models_with_randomness_0.00_%.2f" % unstuckness_high
            args.model_location = "./data/individual_models_with_randomness_0.00_%.2f" % unstuckness_high
            model_option_location = model_location + "/%s-memory_%d-stubbornness_0.00_0.00-randomness_0.00_%.2f-unstuckness_0.00_0.00" % ("deterministic", args.memory, unstuckness_high)
            trial_location = model_option_location + "/max_iterations_180-cliques_6-nodes_per_clique_6-colors_9-q_%.2f" % q
            if not os.path.exists(trial_location):
                os.makedirs(trial_location + "/animation/")
                os.makedirs(trial_location + "/csv/")
                os.makedirs(trial_location + "/component_plot/")
            print(len(os.listdir(trial_location + "/csv/")))
            while len(os.listdir(trial_location + "/csv/")) < trials:
                args.probability_matching = False
                run_trial(args)

        # args.memory = args.memory + 90

        # for unstuckness_high in unstuckness_high_list:
        #     args.randomness_high = unstuckness_high
        #     # model_location = args.model_location
        #     model_location = "./data/individual_models_with_randomness_0.00_%.2f" % unstuckness_high
        #     args.model_location = "./data/individual_models_with_randomness_0.00_%.2f" % unstuckness_high
        #     model_option_location = model_location + "/%s-memory_%d-stubbornness_0.00_0.00-randomness_0.00_%.2f-unstuckness_0.00_0.00" % ("probability_matching", args.memory, unstuckness_high)
        #     trial_location = model_option_location + "/max_iterations_180-cliques_6-nodes_per_clique_6-colors_9-q_%.2f" % q
        #     if not os.path.exists(trial_location):
        #         os.makedirs(trial_location + "/animation/")
        #         os.makedirs(trial_location + "/csv/")
        #         os.makedirs(trial_location + "/component_plot/")
        #     print(len(os.listdir(trial_location + "/csv/")))
        #     while len(os.listdir(trial_location + "/csv/")) < trials:
        #         args.probability_matching = True
        #         run_trial(args)

        # for unstuckness_high in unstuckness_high_list:
        #     args.randomness_high = unstuckness_high
        #     # model_location = args.model_location
        #     model_location = "./data/individual_models_with_randomness_0.00_%.2f" % unstuckness_high
        #     args.model_location = "./data/individual_models_with_randomness_0.00_%.2f" % unstuckness_high
        #     model_option_location = model_location + "/%s-memory_%d-stubbornness_0.00_0.00-randomness_0.00_%.2f-unstuckness_0.00_0.00" % ("probability_matching", args.memory, unstuckness_high)
        #     trial_location = model_option_location + "/max_iterations_180-cliques_6-nodes_per_clique_6-colors_9-q_%.2f" % q
        #     if not os.path.exists(trial_location):
        #         os.makedirs(trial_location + "/animation/")
        #         os.makedirs(trial_location + "/csv/")
        #         os.makedirs(trial_location + "/component_plot/")
        #     print(len(os.listdir(trial_location + "/csv/")))
        #     while len(os.listdir(trial_location + "/csv/")) < trials:
        #         args.probability_matching = False
        #         run_trial(args)


if __name__ == '__main__':

    # parse arguments into trial parameters

    parser = argparse.ArgumentParser()

    # file parameters
    parser.add_argument("--model_location", type=str, default="./data/individual_models/")
    parser.add_argument("--animation", action=argparse.BooleanOptionalAction)
    parser.add_argument("--component_plot", action=argparse.BooleanOptionalAction)
    # note, csv files are always recorded

    # model parameters
    parser.add_argument("--probability_matching", action=argparse.BooleanOptionalAction)
    parser.add_argument("--memory", type=int, default=0)
    parser.add_argument("--stubbornness_low", type=float, default=0.0)
    parser.add_argument("--stubbornness_high", type=float, default=0.0)
    parser.add_argument("--randomness_low", type=float, default=0.0)
    parser.add_argument("--randomness_high", type=float, default=0.0)
    parser.add_argument("--unstuckness_low", type=float, default=0.0)
    parser.add_argument("--unstuckness_high", type=float, default=0.0)

    # trial setup parameters
    parser.add_argument("--max_iterations", type=int, default=180)
    parser.add_argument("--cliques", type=int, default=6)
    parser.add_argument("--nodes_per_clique", type=int, default=6)
    parser.add_argument("--colors", type=int, default=9)
    # parser.add_argument("--q", type=float, default=0) # this will be overwritten

    parser.add_argument("--trials", type=int, default=1)

    args = parser.parse_args()

    trial_args = Namespace(
        model_location = args.model_location,
        animation = args.animation,
        component_plot = args.component_plot,

        probability_matching = args.probability_matching,
        memory = args.memory,
        stubbornness_low = args.stubbornness_low,
        stubbornness_high = args.stubbornness_high,
        randomness_low = args.randomness_low,
        randomness_high = args.randomness_high,
        unstuckness_low = args.unstuckness_low,
        unstuckness_high = args.unstuckness_high,

        max_iterations = args.max_iterations,
        cliques = args.cliques,
        nodes_per_clique = args.nodes_per_clique,
        colors = args.colors,
        q = 0.0 # this will be overwritten
    )

    run_set_of_trials_across_q(trial_args, args.trials)
# imports

from argparse import Namespace
from itertools import product

import argparse
import os


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

    for args in args_options:


        os.system("python run_set_of_trials_for_model_across_q.py "
            + ("--probability_matching " if args[0] else "")
            + "--memory %d " % args[1]
        )
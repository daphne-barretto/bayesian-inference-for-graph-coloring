# imports

from itertools import product

import csv
import matplotlib
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np
import os
import sys


# from https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw=None, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        ax = plt.gca()

    if cbar_kw is None:
        cbar_kw = {}

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    # ax.tick_params(top=True, bottom=False,
                #    labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    plt.xlabel("rewiring probability, q")
    plt.ylabel("memory")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar

# from https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


if __name__ == '__main__':

    plot_individual_models = False
    plot_models_over_memory = True
    plot_heatmaps = False

    csv_file = open("./data/model_comparisons/analysis_avg_solution_time_transparent_180.csv", "r")

    reader = csv.reader(csv_file, delimiter=',')
    rows = list(reader)

    all_model_avg_solution_time = rows[5]
    all_model_avg_solution_time_floats = []

    q_options = [0, 0.1, 0.2, 0.4, 0.6, 1]

    decision_making_calculation_options = ["sum", "product"]
    probability_matching_options = ["deterministic", "probability_matching"]
    memory_options = list(range(0, 181))
    model_options = list(product(decision_making_calculation_options, probability_matching_options, memory_options))

    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

    # plot individual models
    if plot_individual_models:
        i = 0
        for model_option in model_options:
            model_avg_solution_time = list(map(float, all_model_avg_solution_time[i][1:-1].split(", ")))
            print(model_option)
            all_model_avg_solution_time_floats.append(model_avg_solution_time)

            plt.clf()
            fig = plt.figure()
            ax = fig.gca()

            my_cmap = plt.cm.hsv(np.arange(plt.cm.RdBu.N))
            my_cmap[:,0:3] *= 0.8
            my_cmap = ListedColormap(my_cmap)

            plt.gca().set_prop_cycle(plt.cycler('color', my_cmap(np.linspace(0, 1, 181))))

            plt.title("%s, Memory: %d" % (model_option[1], model_option[2]))
            plt.xlabel("rewiring probability, q")
            plt.ylabel("running time (iterations), max 180")

            ax.tick_params(axis="x", direction="in")
            ax.tick_params(axis="y", direction="in")
            ax.xaxis.set_minor_locator(MultipleLocator(0.05))
            ax.tick_params(axis="x", which='minor', direction="in")

            plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0])
            plt.xlim([-0.02, 1.02])
            plt.yticks([0, 30, 60, 90, 120, 150, 180], [0, 30, 60, 90, 120, 150, 180])
            plt.ylim([0, 185])

            plt.plot(q_options, model_avg_solution_time, "o-", label=(("%s-memory_%d")%(model_option[1], model_option[2])))
            plt.legend()
            plt.savefig("./data/model_comparisons/comparison_plots_weighted_average/comparison-%s-memory_%d.png" % (model_option[1], model_option[2]))
            plt.close()

            i += 1

    # plot total models of a type
    if plot_models_over_memory:
        i = 0
        j = 0
        plt.clf()
        # fig, ax = plt.subplots()
        my_cmap = plt.cm.hsv(np.arange(plt.cm.RdBu.N))
        my_cmap[:,0:3] *= 0.8
        my_cmap = ListedColormap(my_cmap)

        plt.gca().set_prop_cycle(plt.cycler('color', my_cmap(np.linspace(0, 1, 181))))
        for decision_making_calculation_option in decision_making_calculation_options:
            for probability_matching_option in probability_matching_options:
                i = 0
                plt.gca().set_prop_cycle(plt.cycler('color', my_cmap(np.linspace(0, 1, 181))))
                # ax = fig.gca()

                # plt.subplot(1, 2, j+1)

                plt.title("%s-%s" % (decision_making_calculation_option, probability_matching_option))
                plt.xlabel("rewiring probability, q")
                plt.ylabel("running time (iterations), max 180")

                # ax.tick_params(axis="x", direction="in")
                # ax.tick_params(axis="y", direction="in")
                # ax.xaxis.set_minor_locator(MultipleLocator(0.05))
                # ax.tick_params(axis="x", which='minor', direction="in")

                plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0])
                plt.xlim([-0.02, 1.02])
                plt.yticks([0, 30, 60, 90, 120, 150, 180], [0, 30, 60, 90, 120, 150, 180])
                plt.ylim([0, 185])

                for memory_option in memory_options:
                    model_avg_solution_time = list(map(float, all_model_avg_solution_time[i + j * 181][1:-1].split(", ")))
                    print(model_avg_solution_time)
                    if (i) % 30 == 0:
                        plt.plot(q_options, model_avg_solution_time, "o-", label=(("memory_%d")%(memory_option)))
                    else:
                        plt.plot(q_options, model_avg_solution_time, "o-", label="_nolegend_")
                    i += 1

                plt.legend()
                # handles, labels = ax.get_legend_handles_labels()
                # ax.legend(handles[::-1], labels[::-1])
                
                plt.savefig("./data/model_comparisons/comparison_plots_transparent_180/comparison-%s-%s.png" % (decision_making_calculation_option, probability_matching_option))
                plt.close()
                j+= 1
    
    # if plot_heatmaps:
    #     i = 0
    #     for probability_matching_option in probability_matching_options:
    #         print(probability_matching_option)
    #         plt.clf()
    #         fig, ax = plt.subplots()
    #         fig.set_size_inches(5, 60)
            
    #         im, cbar = heatmap(np.array(all_model_avg_solution_time_floats[i*181:(i+1)*181]), memory_options, q_options, ax=ax, cmap="RdYlGn_r", cbarlabel="running time (iterations), max 180")
    #         texts = annotate_heatmap(im, valfmt="{x:.0f}")
    #         fig.tight_layout()
    #         plt.savefig("./data/model_comparisons/heatmaps/heatmap_no_colorbar-%s.png" % (probability_matching_option))

    #         i += 1
    
    csv_file.close()
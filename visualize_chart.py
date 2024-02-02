import matplotlib.pyplot as plt
import numpy as np

x = [0.0, 0.1, 0.2, 0.4, 0.6, 1.0]

plt.title("Average Time to Consensus over q for Best Performing Models")
plt.xlabel("rewiring probability, q")
plt.ylabel("average time to consensus (iterations / seconds), max 180")

plt.tick_params(axis="x", direction="in")
plt.tick_params(axis="y", direction="in")
# plt.xaxis.set_minor_locator(MultipleLocator(0.05))
plt.tick_params(axis="x", which='minor', direction="in")

plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.xlim([-0.02, 1.02])
plt.yticks([0, 30, 60, 90, 120, 150, 180], [0, 30, 60, 90, 120, 150, 180])
plt.ylim([0, 185])

# handles, labels = plt.get_legend_handles_labels()
# plt.legend(handles[::-1], labels[::-1])

plt.plot(x, [156.43, 63.57, 50.00, 30.71, 27.85, 18.57], "o-", label="prior behavioral data")

plt.plot(x, [179.2, 102.2, 31.4, 11.266666666666667, 9.566666666666666, 9.833333333333334], "*-", label="theory of mind, product, prob. matching, mem. 0") #0.96
plt.plot(x, [180.0, 180.0, 174.16666666666666, 58.1, 30.666666666666668, 33.56666666666667], "*-", label="theory of mind, product, deterministic, mem. 2") #.070

plt.plot(x, [180.0, 175.67, 109.53, 46.23, 57.13, 85.99], "s-", label="product, prob. matching, mem. 1") #.078
plt.plot(x, [180.0, 180.0, 173.39, 72.52, 24.06, 18.9], "s-", label="product, deterministic, mem. 0") #0.70

plt.plot(x, [180.0, 164.53333333333333, 138.06666666666666, 113.9, 135.16666666666666, 151.93333333333334], "x-", label="decision noise 0.10, product, prob. match, mem. 1") #.075
plt.plot(x, [180.0, 161.8, 112.23333333333333, 67.8, 80.23333333333333, 99.2], "x-", label="stubbornness 0.60, product, prob. match, mem. 1") #0.84
plt.plot(x, [180.0, 177.6, 163.46666666666667, 165.23333333333332, 156.0, 150.4], "x-", label="sub-optimal 0.30, product, deterministic, mem. 1") #0.81

plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.6), ncol=1)
plt.savefig("consensus.png", bbox_inches='tight')
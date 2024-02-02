import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = [0.67,0.77,0.30,0.67,1.00,0.67,0.87,0.57,0.03,0.10,0.70,0.07,0.97,0.50,0.90,0.97,1.00,0.10,0.63,0.97,0.73,1.00,0.47,0.47,0.46,0.03,0.80,0.97,1.00,0.93,0.97,0.33,0.23,0.00,1.00,0.60,0.97,0.00,0.90,0.80,0.73,0.83,0.70,0.97,0.93,0.03,1.00,0.80,0.40,0.53,0.43,0.60,1.00,0.93,0.90,0.30,0.57,0.70,0.80,0.73,0.53,0.50,0.93,0.77,1.00,0.30,0.30,0.40,0.72,0.43,0.83,0.73,0.97,0.03,0.83,0.70,0.83,0.97,0.83,0.07,0.00,0.97,0.97,0.57,0.43,0.50,0.70,0.97,1.00,0.93,0.43,0.50,0.93,1.00,0.00,1.00,0.33,0.43,0.30,1.00,1.00,1.00,0.67,1.00,0.57,1.00,1.00]

# Set up the histogram
bins = np.arange(0, 1.11, 0.1)
plt.hist(data, bins=bins)

# Set up the plot title and axis labels
plt.title("Number of Participants across Mean Participant Theory of Mindedness Values")
plt.xlabel("Mean Participant Theory of Mindedness Value")
plt.ylabel("Number of Participants")

# Set up the y-axis and x-axis intervals
plt.yticks(np.arange(0, 26, 5))
plt.xticks(np.arange(0, 1.1, 0.1))

# Show the plot
plt.show()

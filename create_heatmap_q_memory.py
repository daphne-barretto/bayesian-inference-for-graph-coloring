import matplotlib.pyplot as plt
import numpy as np

q_options = [0, 0.1, 0.2, 0.4, 0.6, 1]
memory_options = [0, 1, 2, 3, 100]

data = np.array([   
    [60., 60.,          60., 33.18, 19.46938776, 12.], 
    [60., 60.,          58.96, 40.04, 17.6122449, 13.95833333],
    [60., 60.,          60., 46.01333333, 21.87248322, 17.14285714], 
    [60., 60.,          60., 43.14, 26.5, 21.25], 
    [60., 60.,          60., 58.02020202, 50.78350515, 40.0106383 ]
])

fig, ax = plt.subplots()
im = ax.imshow(data)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(q_options)), labels=q_options)
ax.set_yticks(np.arange(len(memory_options)), labels=memory_options)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(memory_options)):
    for j in range(len(q_options)):
        text = ax.text(j, i, data[i, j],
                       ha="center", va="center", color="w")

ax.set_title("q v memory")
fig.tight_layout()
plt.savefig("heatmap1.png")
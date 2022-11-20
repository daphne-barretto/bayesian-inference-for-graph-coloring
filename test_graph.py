import matplotlib.animation as animation
import matplotlib.pyplot as plt
import networkx as nx

G = nx.complete_graph(9)

def animate(frame):
    ax = plt.gca()
    ax.set_title("Time " + str(frame))
    # nc = [default_colors[x] for x in trial_node_color_history[frame]]
    nc = range(9)
    nodes.set_array(nc)
    return nodes,

# %% layout and draw graph

pos = nx.spring_layout(G)
nodes = nx.draw_networkx_nodes(G, pos, cmap="tab10", node_color=range(9))
edges = nx.draw_networkx_edges(G, pos)
edges = nx.draw_networkx_labels(G, pos)
plt.axis('off')

fig = plt.gcf()
ani = animation.FuncAnimation(fig, animate, interval=500, frames=6, blit=True)

file_name = "./test.gif"
ani.save(file_name)
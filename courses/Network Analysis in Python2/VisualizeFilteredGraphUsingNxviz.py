/* Here, you'll visualize the filtered graph using a CircosPlot. The CircosPlot is a natural choice for this visualization, as you can use node grouping and coloring to visualize the partitions, while the circular layout preserves the aesthetics of the visualization. */

# Import necessary modules
from nxviz import CircosPlot
import networkx as nx
import matplotlib.pyplot as plt

# Compute degree centrality scores of each node
dcs = nx.bipartite.degree_centrality(G, nodes=forum_nodes)
for n, d in G_sub.nodes(data=True):
    G_sub.node[n]['dc'] = dcs[n]

# Create the CircosPlot object: c
c = CircosPlot(G_sub, node_color='bipartite', node_grouping='bipartite', node_order='dc')

# Draw c to screen
c.draw()

# Display the plot
plt.show() 

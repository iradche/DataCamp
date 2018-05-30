/* The last exercise was on degree centrality; this time round, let's recall betweenness centrality!

A small note: if executed correctly, this exercise may need about 5 seconds to execute. */

# Import necessary modules
import matplotlib.pyplot as plt
import networkx as nx

# Plot the degree distribution of the GitHub collaboration network
plt.hist(list(nx.betweenness_centrality(G).values()))
plt.show()

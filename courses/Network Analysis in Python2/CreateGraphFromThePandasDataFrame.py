/* Let's start by creating a graph from a pandas DataFrame. In this exercise, you'll create a new bipartite graph by looping over the edgelist (which is a DataFrame object).

For simplicity's sake, in this graph construction procedure, any edge between a student and a forum node will be the 'last' edge (in time) that a student posted to a forum over the entire time span of the dataset, though there are ways to get around this.

Additionally, to shorten the runtime of the exercise, we have provided a sub-sampled version of the edge list as data. Explore it in the IPython Shell to familiarize yourself with it. */

import networkx as nx

# Instantiate a new Graph: G
G = nx.Graph()

# Add nodes from each of the partitions
G.add_nodes_from(data['student'], bipartite = 'student')
G.add_nodes_from(data['forum'], bipartite = 'forum')

# Add in each edge along with the date the edge was created
for r, d in data.iterrows():
    G.add_edge(d['student'], d['forum'], date=d['date']) 

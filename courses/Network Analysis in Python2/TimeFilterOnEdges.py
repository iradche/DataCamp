/* You're now going to practice filtering the graph using a conditional as applied to the edges. This will help you gain practice and become comfortable with list comprehensions that contain conditionals.

To help you with the exercises, remember that you can import datetime objects from the datetime module. On the graph, the metadata has a date key that is paired with a datetime object as a value. */

import networkx as nx
from datetime import datetime

# Instantiate a new graph: G_sub
G_sub = nx.Graph()

# Add nodes from the original graph
G_sub.add_nodes_from(G.nodes(data=True)) 

# Add edges using a list comprehension with one conditional on the edge dates, that the date of the edge is earlier than 2004-05-16.
G_sub.add_edges_from([(u, v, d) for u, v, d in G.edges(data=True) if d['date'] < datetime(2004, 5, 16)])

/* It's now time to to try your hand at computing the projection of a bipartite graph to the nodes on one of its partitions. This will help you gain practice with converting between a bipartite version of a graph and its unipartite projections. Remember from the video that the "projection" of a graph onto one of its partitions is the connectivity of the nodes in that partition conditioned on connections to nodes on the other partition. Made more concretely, you can think of the "connectivity of customers based on shared purchases".

To help you get started, here's a hint on list comprehensions. List comprehensions can include conditions, so if you want to filter a graph for a certain type of node, you can do: [n for n, d in G.nodes(data=True) if d['key'] == 'some_value'] */

# Prepare the nodelists needed for computing projections: people, clubs
people = [n for n in G.nodes() if G.node[n]['bipartite'] == 'people']
clubs = [n for n, d in G.nodes(data=True) if d['bipartite'] == 'clubs']

# Compute the people and clubs projections: peopleG, clubsG
peopleG = nx.bipartite.projected_graph(G, people)
clubsG = nx.bipartite.projected_graph(G, clubs)

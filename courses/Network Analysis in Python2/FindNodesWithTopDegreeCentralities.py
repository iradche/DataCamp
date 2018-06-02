/* In this exercise, you'll take a deeper dive to see whether there's anything interesting about the most connected students in the network. First off, you'll find the cluster of students that have the highest degree centralities. This result will be saved for the next plotting exercise. */

# Get the top 5 unique degree centrality scores: top_dcs
top_dcs = sorted(set(nx.degree_centrality(G).values()), reverse=True)[0:5]

# Create list of nodes that have the top 5 highest overall degree centralities
top_connected = []
for n, dc in nx.degree_centrality(G).items():
    if dc in top_dcs:
        top_connected.append(n)
        
# Print the number of nodes that share the top 5 degree centrality scores
print(len(top_connected))

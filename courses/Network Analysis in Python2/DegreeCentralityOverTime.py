/*  Now, you're going to plot the degree centrality distribution over time. Remember that the ECDF function will be provided, so you won't have to implement it. */

# Import necessary modules
import networkx as nx
import matplotlib.pyplot as plt

# Create a list of degree centrality scores month-by-month
cents = []
for G in Gs:
    cent = nx.degree_centrality(G)
    cents.append(cent)

# Plot ECDFs over time
fig = plt.figure()
for i in range(len(cents)):
    x, y = ECDF(cents[i].values())
    plt.plot(x, y, label='Month {0}'.format(i+1)) 
plt.legend()   
plt.show()
